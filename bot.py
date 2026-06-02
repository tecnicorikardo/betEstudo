from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import threading
import time
import unicodedata
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parent
DEFAULT_SCHEDULE_FILE = ROOT_DIR / "cronograma_ti_20_semanas_detalhado.md"
DEFAULT_ENGLISH_SCHEDULE_FILE = ROOT_DIR / "Guia Completo_ Frases do Cotidiano Americano.md"
DEFAULT_GRAMMAR_SCHEDULE_FILE = ROOT_DIR / "gramatica.md"
DEFAULT_BIBLE_SCHEDULE_FILE = ROOT_DIR / "resumo_novo_testamento.md"
DEFAULT_BIBLE_SCHEDULE_URL = (
    "https://raw.githubusercontent.com/tecnicorikardo/betEstudo/main/resumo_novo_testamento.md"
)
LOCAL_TOKEN_FILE = ROOT_DIR / "token telegram.txt"
SUBSCRIBERS_FILE = ROOT_DIR / "subscribers.json"

TITLE_RE = re.compile(r"^#\s+(?!#)(.+?)\s*$")
MODULE_RE = re.compile(r"^##\s+(?!#)(.+?)\s*$")
WEEK_RE = re.compile(r"^###\s+Semana\s+(\d+)\b\s*(?:[-\u2013]\s*)?(.*)$")
LESSON_RE = re.compile(r"^####\s+([^:]+):\s*(.+?)\s*$")
WEEKDAY_SECTION_RE = re.compile(
    r"^#{2,6}\s+(?:[^\wÀ-ÿ]+)?\**(?P<day>segunda-feira|terca-feira|terça-feira|quarta-feira|quinta-feira|sexta-feira)\**\s*(?::|[-\u2013])\s*\**(?P<title>.+?)\**\s*$",
    re.IGNORECASE,
)
BIBLE_CHAPTER_RE = re.compile(
    r"^(?:resumo\s+(?:de\s+)?)?(?P<title>[1-3]?\s*[A-Za-zÀ-ÿ]+(?:\s+[A-Za-zÀ-ÿ]+)*\s*(?:[-\u2013:]\s*)?(?:cap[ií]tulo\s*)?\d+)\b.*$",
    re.IGNORECASE,
)

WEEKDAY_NAMES = {
    0: "Segunda-feira",
    1: "Terca-feira",
    2: "Quarta-feira",
    3: "Quinta-feira",
    4: "Sexta-feira",
}

WEEKDAY_KEYS = {
    "segunda-feira": 0,
    "segunda": 0,
    "terca-feira": 1,
    "terca": 1,
    "quarta-feira": 2,
    "quarta": 2,
    "quinta-feira": 3,
    "quinta": 3,
    "sexta-feira": 4,
    "sexta": 4,
}


@dataclass(frozen=True)
class Lesson:
    module: str
    week: int
    week_title: str
    weekday: int
    weekday_name: str
    title: str
    body: str


class ConfigError(RuntimeError):
    pass


class TelegramApiError(RuntimeError):
    pass


class GroqApiError(RuntimeError):
    def __init__(self, message: str, status_code: int | None = None):
        super().__init__(message)
        self.status_code = status_code


class DeepSeekApiError(RuntimeError):
    def __init__(self, message: str, status_code: int | None = None):
        super().__init__(message)
        self.status_code = status_code


def parse_bool(value: str, default: bool = False) -> bool:
    normalized = value.strip().lower()
    if not normalized:
        return default
    return normalized in {"1", "true", "yes", "y", "sim", "s", "on"}


def configure_stdout() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def normalize_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value.strip().lower())
    return "".join(char for char in normalized if not unicodedata.combining(char))


def parse_date(value: str) -> date:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ConfigError("SCHEDULE_START_DATE deve usar o formato YYYY-MM-DD.") from exc


def read_token() -> str:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    if token:
        return token

    if LOCAL_TOKEN_FILE.exists():
        return LOCAL_TOKEN_FILE.read_text(encoding="utf-8").strip()

    raise ConfigError("Configure TELEGRAM_BOT_TOKEN no Railway ou crie o arquivo local de token.")


def read_start_date() -> date:
    value = os.getenv("SCHEDULE_START_DATE", "").strip()
    if not value:
        raise ConfigError("Configure SCHEDULE_START_DATE com a data da Semana 1, Segunda-feira.")

    start_date = parse_date(value)
    if start_date.weekday() != 0:
        raise ConfigError("SCHEDULE_START_DATE precisa cair em uma segunda-feira.")

    return start_date


def schedule_path() -> Path:
    configured = os.getenv("SCHEDULE_FILE", "").strip()
    if not configured:
        return DEFAULT_SCHEDULE_FILE
    path = Path(configured)
    return path if path.is_absolute() else ROOT_DIR / path


def english_schedule_path() -> Path:
    configured = os.getenv("ENGLISH_SCHEDULE_FILE", "").strip()
    if not configured:
        return DEFAULT_ENGLISH_SCHEDULE_FILE
    path = Path(configured)
    return path if path.is_absolute() else ROOT_DIR / path


def grammar_schedule_path() -> Path:
    configured = os.getenv("GRAMMAR_SCHEDULE_FILE", "").strip()
    if not configured:
        return DEFAULT_GRAMMAR_SCHEDULE_FILE
    path = Path(configured)
    return path if path.is_absolute() else ROOT_DIR / path


def bible_schedule_path() -> Path:
    configured = os.getenv("BIBLE_SCHEDULE_FILE", "").strip()
    if not configured:
        path = DEFAULT_BIBLE_SCHEDULE_FILE
    else:
        path = Path(configured)
        path = path if path.is_absolute() else ROOT_DIR / path

    if path.exists():
        return path

    fallback = find_file_case_insensitive(ROOT_DIR, path.name)
    if fallback:
        return fallback

    return path


def find_file_case_insensitive(directory: Path, filename: str) -> Path | None:
    expected = filename.lower()
    for item in directory.glob("*.md"):
        if item.name.lower() == expected:
            return item
    return None


def ensure_bible_schedule_file(path: Path) -> Path:
    if path.exists():
        return path

    url = os.getenv("BIBLE_SCHEDULE_URL", DEFAULT_BIBLE_SCHEDULE_URL).strip()
    if not url:
        return path

    logging.warning("Cronograma biblico nao encontrado em %s. Tentando baixar de BIBLE_SCHEDULE_URL.", path)
    response = requests.get(url, timeout=30)
    if response.ok and response.text.strip():
        path.write_text(response.text, encoding="utf-8")
        logging.info("Cronograma biblico baixado para %s.", path)
        return path

    logging.error("Falha ao baixar cronograma biblico: HTTP %s.", response.status_code)
    return path


def parse_schedule(path: Path) -> list[Lesson]:
    if not path.exists():
        raise ConfigError(f"Cronograma nao encontrado: {path}")

    lessons: list[Lesson] = []
    current_module = ""
    current_week = 0
    current_week_title = ""
    current_lesson: dict[str, object] | None = None
    current_body: list[str] = []

    def flush_lesson() -> None:
        nonlocal current_lesson, current_body
        if not current_lesson:
            return

        body = "\n".join(current_body).strip()
        lessons.append(
            Lesson(
                module=str(current_lesson["module"]),
                week=int(current_lesson["week"]),
                week_title=str(current_lesson["week_title"]),
                weekday=int(current_lesson["weekday"]),
                weekday_name=str(current_lesson["weekday_name"]),
                title=str(current_lesson["title"]),
                body=body,
            )
        )
        current_lesson = None
        current_body = []

    for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
        module_match = MODULE_RE.match(raw_line)
        if module_match:
            flush_lesson()
            current_module = module_match.group(1)
            continue

        week_match = WEEK_RE.match(raw_line)
        if week_match:
            flush_lesson()
            current_week = int(week_match.group(1))
            current_week_title = week_match.group(2).strip()
            continue

        lesson_match = LESSON_RE.match(raw_line)
        if lesson_match:
            day_key = normalize_text(lesson_match.group(1))
            weekday = WEEKDAY_KEYS.get(day_key)
            if weekday is None:
                continue

            flush_lesson()
            current_lesson = {
                "module": current_module,
                "week": current_week,
                "week_title": current_week_title,
                "weekday": weekday,
                "weekday_name": WEEKDAY_NAMES[weekday],
                "title": lesson_match.group(2).strip(),
            }
            continue

        if current_lesson:
            current_body.append(raw_line)

    flush_lesson()

    lessons.sort(key=lambda item: (item.week, item.weekday))
    return lessons


def parse_bible_schedule(path: Path) -> list[Lesson]:
    try:
        path = ensure_bible_schedule_file(path)
    except requests.RequestException as exc:
        logging.error("Falha de rede ao buscar cronograma biblico: %s", exc.__class__.__name__)

    if not path.exists():
        raise ConfigError(f"Cronograma biblico nao encontrado: {path}")

    lessons: list[Lesson] = []
    document_title = "Resumo do Novo Testamento"
    current_book = ""
    current_title = ""
    current_body: list[str] = []
    seen_titles: set[str] = set()

    def clean_cell(value: str) -> str:
        cleaned = value.strip()
        cleaned = re.sub(r"^\*\*(.+?)\*\*$", r"\1", cleaned)
        return cleaned.strip()

    def add_chapter(title: str, body: str) -> None:
        normalized_title = normalize_text(title)
        if normalized_title in seen_titles:
            logging.warning("Capitulo biblico duplicado ignorado: %s", title)
            return

        seen_titles.add(normalized_title)
        chapter_number = len(lessons) + 1
        lessons.append(
            Lesson(
                module=document_title,
                week=(chapter_number - 1) // 7 + 1,
                week_title="Novo Testamento",
                weekday=(chapter_number - 1) % 7,
                weekday_name="Diario",
                title=title,
                body=body.strip(),
            )
        )

    def flush_chapter() -> None:
        nonlocal current_title, current_body
        if not current_title:
            return

        add_chapter(current_title, "\n".join(current_body))
        current_title = ""
        current_body = []

    for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
        title_match = TITLE_RE.match(raw_line)
        if title_match:
            flush_chapter()
            current_book = title_match.group(1).strip()
            continue

        heading_match = re.match(r"^#{1,6}\s+(.+?)\s*$", raw_line)
        if heading_match:
            heading = heading_match.group(1).strip()
            chapter_match = BIBLE_CHAPTER_RE.match(heading)
            if chapter_match:
                flush_chapter()
                current_title = chapter_match.group("title").strip()
                continue

        if raw_line.strip().startswith("|") and current_book:
            cells = [clean_cell(cell) for cell in raw_line.strip().strip("|").split("|")]
            if not cells or all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                continue

            first_cell = normalize_text(cells[0])
            if first_cell in {"capitulo", "tema principal"}:
                continue

            if len(cells) >= 3 and re.fullmatch(r"\d+", cells[0]):
                title = f"{current_book} {cells[0]}"
                body = f"Tema principal: {cells[1]}\n\nResumo: {' | '.join(cells[2:])}"
                add_chapter(title, body)
                continue

            if len(cells) >= 2 and cells[0] and cells[1]:
                title = f"{current_book} 1"
                body = f"Tema principal: {cells[0]}\n\nResumo: {' | '.join(cells[1:])}"
                add_chapter(title, body)
                continue

        if current_title:
            current_body.append(raw_line)

    flush_chapter()
    return lessons


def parse_weekday_schedule(path: Path) -> dict[int, Lesson]:
    if not path.exists():
        raise ConfigError(f"Cronograma de ingles nao encontrado: {path}")

    lessons: dict[int, Lesson] = {}
    document_title = path.stem
    current_lesson: dict[str, object] | None = None
    current_body: list[str] = []

    def flush_lesson() -> None:
        nonlocal current_lesson, current_body
        if not current_lesson:
            return

        lesson = Lesson(
            module=str(current_lesson["module"]),
            week=1,
            week_title="Ciclo semanal",
            weekday=int(current_lesson["weekday"]),
            weekday_name=str(current_lesson["weekday_name"]),
            title=str(current_lesson["title"]),
            body="\n".join(current_body).strip(),
        )
        lessons[lesson.weekday] = lesson
        current_lesson = None
        current_body = []

    for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
        title_match = TITLE_RE.match(raw_line)
        if title_match:
            document_title = title_match.group(1)
            continue

        section_match = WEEKDAY_SECTION_RE.match(raw_line)
        if section_match:
            day_key = normalize_text(section_match.group("day"))
            weekday = WEEKDAY_KEYS.get(day_key)
            if weekday is not None:
                flush_lesson()
                current_lesson = {
                    "module": document_title,
                    "weekday": weekday,
                    "weekday_name": WEEKDAY_NAMES[weekday],
                    "title": section_match.group("title").strip().strip("*"),
                }
                continue

            flush_lesson()
            continue

        if current_lesson:
            current_body.append(raw_line)

    flush_lesson()
    return lessons


def lesson_for_date(lessons: list[Lesson], start_date: date, target_date: date) -> Lesson | None:
    if target_date < start_date or target_date.weekday() > 4:
        return None

    elapsed_days = (target_date - start_date).days
    lesson_index = (elapsed_days // 7) * 5 + target_date.weekday()
    if lesson_index >= len(lessons):
        return None

    return lessons[lesson_index]


def weekday_lesson_for_date(lessons: dict[int, Lesson], target_date: date) -> Lesson | None:
    if target_date.weekday() > 4:
        return None
    return lessons.get(target_date.weekday())


def sequential_lesson_for_date(lessons: list[Lesson], start_date: date, target_date: date) -> Lesson | None:
    if target_date < start_date or not lessons:
        return None

    lesson_index = (target_date - start_date).days
    if lesson_index >= len(lessons):
        return None

    return lessons[lesson_index]


def format_lesson(lesson: Lesson, target_date: date) -> str:
    header = "\n".join(
        [
            "Aula de hoje",
            f"Data: {target_date:%d/%m/%Y}",
            f"Modulo: {lesson.module}",
            f"Semana {lesson.week}: {lesson.week_title}",
            f"Dia: {lesson.weekday_name}",
            f"Tema: {lesson.title}",
            "",
            "Conteudo:",
        ]
    )

    if not lesson.body:
        return header

    return f"{header}\n{lesson.body}"


def format_bible_lesson(lesson: Lesson, target_date: date, body: str | None = None) -> str:
    content = body if body is not None else lesson.body
    header = "\n".join(
        [
            "Resumo biblico de hoje",
            f"Data: {target_date:%d/%m/%Y}",
            f"Serie: {lesson.module}",
            f"Capitulo: {lesson.title}",
            "",
            "Conteudo:",
        ]
    )

    if not content:
        return header

    return f"{header}\n{content}"


def format_english_lesson(lesson: Lesson, target_date: date) -> str:
    header = "\n".join(
        [
            "Ingles de hoje",
            f"Data: {target_date:%d/%m/%Y}",
            f"Guia: {lesson.module}",
            f"Dia: {lesson.weekday_name}",
            f"Tema: {lesson.title}",
            "",
            "Conteudo:",
        ]
    )

    if not lesson.body:
        return header

    return f"{header}\n{lesson.body}"


def format_grammar_lesson(lesson: Lesson, target_date: date) -> str:
    header = "\n".join(
        [
            "Gramatica de ingles de hoje",
            f"Data: {target_date:%d/%m/%Y}",
            f"Guia: {lesson.module}",
            f"Dia: {lesson.weekday_name}",
            f"Tema: {lesson.title}",
            "",
            "Conteudo:",
        ]
    )

    if not lesson.body:
        return header

    return f"{header}\n{lesson.body}"


def split_message(text: str, limit: int = 3900) -> list[str]:
    if len(text) <= limit:
        return [text]

    chunks: list[str] = []
    remaining = text
    while len(remaining) > limit:
        split_at = remaining.rfind("\n\n", 0, limit)
        if split_at < limit * 0.5:
            split_at = remaining.rfind("\n", 0, limit)
        if split_at < limit * 0.5:
            split_at = limit

        chunks.append(remaining[:split_at].strip())
        remaining = remaining[split_at:].strip()

    if remaining:
        chunks.append(remaining)

    total = len(chunks)
    if total == 1:
        return chunks

    return [f"Parte {index}/{total}\n\n{chunk}" for index, chunk in enumerate(chunks, start=1)]


def telegram_api_url(token: str, method: str) -> str:
    return f"https://api.telegram.org/bot{token}/{method}"


def raise_for_telegram(response: requests.Response, action: str) -> None:
    if response.ok:
        return

    description = response.text
    try:
        payload = response.json()
        description = payload.get("description", description)
    except ValueError:
        pass

    raise TelegramApiError(f"{action} falhou: HTTP {response.status_code} - {description}")


def groq_api_key() -> str:
    return os.getenv("GROQ_API_KEY", "").strip()


def deep_api_key() -> str:
    return os.getenv("DEEP_API_KEY", os.getenv("DEEPSEEK_API_KEY", "")).strip()


def active_ai_provider() -> str | None:
    if deep_api_key():
        return "deepseek"
    if groq_api_key():
        return "groq"
    return None


def deepseek_chat_completion(messages: list[dict[str, str]]) -> str:
    api_key = deep_api_key()
    if not api_key:
        raise DeepSeekApiError("DEEP_API_KEY nao configurada.")

    base_url = os.getenv("DEEP_BASE_URL", "https://api.deepseek.com").rstrip("/")
    response = requests.post(
        f"{base_url}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": os.getenv("DEEP_MODEL", "deepseek-v4-flash"),
            "messages": messages,
            "thinking": {"type": os.getenv("DEEP_THINKING", "disabled")},
            "temperature": float(os.getenv("DEEP_TEMPERATURE", os.getenv("GROQ_TEMPERATURE", "0.4"))),
            "max_tokens": int(os.getenv("DEEP_MAX_TOKENS", os.getenv("GROQ_MAX_TOKENS", "700"))),
        },
        timeout=60,
    )

    if not response.ok:
        description = response.text
        try:
            payload = response.json()
            description = payload.get("error", {}).get("message", description)
        except ValueError:
            pass
        raise DeepSeekApiError(f"DeepSeek falhou: HTTP {response.status_code} - {description}", response.status_code)

    payload = response.json()
    return payload["choices"][0]["message"]["content"].strip()


def groq_chat_completion(messages: list[dict[str, str]]) -> str:
    api_key = groq_api_key()
    if not api_key:
        raise GroqApiError("GROQ_API_KEY nao configurada.")

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
            "messages": messages,
            "temperature": float(os.getenv("GROQ_TEMPERATURE", "0.4")),
            "max_tokens": int(os.getenv("GROQ_MAX_TOKENS", "700")),
        },
        timeout=60,
    )

    if not response.ok:
        description = response.text
        try:
            payload = response.json()
            description = payload.get("error", {}).get("message", description)
        except ValueError:
            pass
        raise GroqApiError(f"Groq falhou: HTTP {response.status_code} - {description}", response.status_code)

    payload = response.json()
    return payload["choices"][0]["message"]["content"].strip()


def ai_chat_completion(messages: list[dict[str, str]]) -> str:
    provider = active_ai_provider()
    if provider == "deepseek":
        return deepseek_chat_completion(messages)
    if provider == "groq":
        return groq_chat_completion(messages)
    raise DeepSeekApiError("Nenhuma IA configurada. Configure DEEP_API_KEY ou GROQ_API_KEY.")


def enhance_bible_summary_with_ai(lesson: Lesson) -> str:
    if not active_ai_provider():
        return lesson.body

    prompt = (
        "Transforme o resumo abaixo em uma mensagem diaria para Telegram, em portugues do Brasil. "
        "Seja claro, respeitoso e fiel ao conteudo biblico. Organize em: 1) resumo do capitulo, "
        "2) mensagem principal, 3) aplicacao pratica para hoje. Nao invente versiculos nem fatos "
        "que nao estejam no texto. Mantenha entre 120 e 220 palavras.\n\n"
        f"Capitulo: {lesson.title}\n\n"
        f"Resumo base:\n{lesson.body}"
    )
    return ai_chat_completion(
        [
            {
                "role": "system",
                "content": (
                    "Voce e um assistente de estudos biblicos. Responda com linguagem simples, "
                    "devocional leve e foco em compreensao do Novo Testamento."
                ),
            },
            {"role": "user", "content": prompt},
        ]
    )


def ask_ai(question: str) -> str:
    return ai_chat_completion(
        [
            {
                "role": "system",
                "content": (
                    "Voce e o assistente do bot BetEstudo. Responda em portugues do Brasil, "
                    "com clareza, objetividade e tom respeitoso. Ajude em estudos de TI, ingles "
                    "e resumos biblicos quando solicitado."
                ),
            },
            {"role": "user", "content": question},
        ]
    )


def ai_error_message(exc: Exception) -> str:
    if isinstance(exc, DeepSeekApiError):
        message = str(exc).lower()
        if "nenhuma ia configurada" in message:
            return "A IA nao esta configurada no Railway. Configure DEEP_API_KEY ou GROQ_API_KEY."
        if "nao configurada" in message:
            return "A DeepSeek nao esta configurada no Railway. Confira se existe a variavel DEEP_API_KEY com a chave real."
        if exc.status_code in {401, 403}:
            return "A DeepSeek recusou a chave configurada. Confira se a DEEP_API_KEY esta correta, ativa e sem espacos ou aspas."
        if exc.status_code == 404 or "model" in message:
            return "A DeepSeek recusou o modelo configurado. Confira a variavel DEEP_MODEL no Railway."
        if exc.status_code == 429:
            return "A DeepSeek bloqueou por limite de uso ou muitas requisicoes. Tente novamente em alguns minutos."
        if exc.status_code and exc.status_code >= 500:
            return "A DeepSeek esta instavel agora. Tente novamente em alguns minutos."
    if isinstance(exc, GroqApiError):
        message = str(exc).lower()
        if "nao configurada" in message:
            return "A IA nao esta configurada no Railway. Confira se existe a variavel GROQ_API_KEY com a chave real da Groq."
        if exc.status_code in {401, 403}:
            return "A Groq recusou a chave configurada. Confira se a GROQ_API_KEY esta correta, ativa e sem espacos ou aspas."
        if exc.status_code == 404 or "model" in message:
            return "A Groq recusou o modelo configurado. Confira a variavel GROQ_MODEL no Railway."
        if exc.status_code == 429:
            return "A Groq bloqueou por limite de uso ou muitas requisicoes. Tente novamente em alguns minutos."
        if exc.status_code and exc.status_code >= 500:
            return "A Groq esta instavel agora. Tente novamente em alguns minutos."
    if isinstance(exc, requests.RequestException):
        return "Nao consegui conectar na IA agora. Tente novamente em alguns minutos."
    return "Nao consegui responder com a IA agora. Confira as variaveis DEEP_API_KEY ou GROQ_API_KEY no Railway."


def send_telegram_message(token: str, chat_id: str, text: str) -> None:
    response = requests.post(
        telegram_api_url(token, "sendMessage"),
        json={
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": True,
        },
        timeout=30,
    )
    raise_for_telegram(response, "sendMessage")


def load_subscribers() -> set[str]:
    configured = {
        chat_id.strip()
        for chat_id in os.getenv("TELEGRAM_CHAT_IDS", "").replace(";", ",").split(",")
        if chat_id.strip()
    }

    if not SUBSCRIBERS_FILE.exists():
        return configured

    try:
        stored = json.loads(SUBSCRIBERS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        logging.warning("Nao foi possivel ler subscribers.json.")
        return configured

    if isinstance(stored, list):
        configured.update(str(item) for item in stored if str(item).strip())

    return configured


def save_subscriber(chat_id: str) -> None:
    subscribers = load_subscribers()
    subscribers.add(str(chat_id))
    SUBSCRIBERS_FILE.write_text(
        json.dumps(sorted(subscribers), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def send_lesson_to_subscribers(token: str, lessons: list[Lesson], start_date: date, target_date: date) -> None:
    lesson = lesson_for_date(lessons, start_date, target_date)
    if not lesson:
        logging.info("Nenhuma aula programada para %s.", target_date.isoformat())
        return

    subscribers = load_subscribers()
    if not subscribers:
        logging.warning("Nenhum TELEGRAM_CHAT_IDS configurado e nenhum /start recebido.")
        return

    text = format_lesson(lesson, target_date)
    chunks = split_message(text)

    for chat_id in subscribers:
        for chunk in chunks:
            try:
                send_telegram_message(token, chat_id, chunk)
            except (requests.RequestException, TelegramApiError) as exc:
                logging.error("Falha ao enviar aula para chat_id=%s: %s", chat_id, exc)
                break
            time.sleep(0.4)
        else:
            logging.info("Aula enviada para chat_id=%s.", chat_id)


def send_weekday_lesson_to_subscribers(
    token: str,
    lessons: dict[int, Lesson],
    target_date: date,
) -> None:
    lesson = weekday_lesson_for_date(lessons, target_date)
    if not lesson:
        logging.info("Nenhuma aula de ingles programada para %s.", target_date.isoformat())
        return

    subscribers = load_subscribers()
    if not subscribers:
        logging.warning("Nenhum TELEGRAM_CHAT_IDS configurado para envio de ingles.")
        return

    chunks = split_message(format_english_lesson(lesson, target_date))
    for chat_id in subscribers:
        for chunk in chunks:
            try:
                send_telegram_message(token, chat_id, chunk)
            except (requests.RequestException, TelegramApiError) as exc:
                logging.error("Falha ao enviar ingles para chat_id=%s: %s", chat_id, exc)
                break
            time.sleep(0.4)
        else:
            logging.info("Aula de ingles enviada para chat_id=%s.", chat_id)


def send_grammar_lesson_to_subscribers(
    token: str,
    lessons: dict[int, Lesson],
    target_date: date,
) -> None:
    lesson = weekday_lesson_for_date(lessons, target_date)
    if not lesson:
        logging.info("Nenhuma aula de gramatica programada para %s.", target_date.isoformat())
        return

    subscribers = load_subscribers()
    if not subscribers:
        logging.warning("Nenhum TELEGRAM_CHAT_IDS configurado para envio de gramatica.")
        return

    chunks = split_message(format_grammar_lesson(lesson, target_date))
    for chat_id in subscribers:
        for chunk in chunks:
            try:
                send_telegram_message(token, chat_id, chunk)
            except (requests.RequestException, TelegramApiError) as exc:
                logging.error("Falha ao enviar gramatica para chat_id=%s: %s", chat_id, exc)
                break
            time.sleep(0.4)
        else:
            logging.info("Aula de gramatica enviada para chat_id=%s.", chat_id)


def send_bible_lesson_to_subscribers(
    token: str,
    lessons: list[Lesson],
    start_date: date,
    target_date: date,
) -> None:
    lesson = sequential_lesson_for_date(lessons, start_date, target_date)
    if not lesson:
        logging.info("Nenhum resumo biblico programado para %s.", target_date.isoformat())
        return

    subscribers = load_subscribers()
    if not subscribers:
        logging.warning("Nenhum TELEGRAM_CHAT_IDS configurado para envio biblico.")
        return

    try:
        body = enhance_bible_summary_with_ai(lesson)
    except (requests.RequestException, DeepSeekApiError, GroqApiError, KeyError, IndexError) as exc:
        logging.error("Falha ao usar IA para %s: %s. Enviando resumo original.", lesson.title, exc)
        body = lesson.body

    chunks = split_message(format_bible_lesson(lesson, target_date, body))
    for chat_id in subscribers:
        for chunk in chunks:
            try:
                send_telegram_message(token, chat_id, chunk)
            except (requests.RequestException, TelegramApiError) as exc:
                logging.error("Falha ao enviar biblico para chat_id=%s: %s", chat_id, exc)
                break
            time.sleep(0.4)
        else:
            logging.info("Resumo biblico enviado para chat_id=%s.", chat_id)


def reply(token: str, chat_id: str, text: str) -> None:
    try:
        send_telegram_message(token, chat_id, text)
    except (requests.RequestException, TelegramApiError) as exc:
        logging.error("Falha ao responder chat_id=%s: %s", chat_id, exc)


def polling_loop(
    token: str,
    lessons: list[Lesson],
    start_date: date,
    english_lessons: dict[int, Lesson],
    grammar_lessons: dict[int, Lesson],
    bible_lessons: list[Lesson],
    bible_start_date: date,
    timezone: ZoneInfo,
) -> None:
    offset: int | None = None
    logging.info("Polling do Telegram iniciado.")

    while True:
        try:
            response = requests.get(
                telegram_api_url(token, "getUpdates"),
                params={"timeout": 30, "offset": offset},
                timeout=40,
            )
            raise_for_telegram(response, "getUpdates")
            updates = response.json().get("result", [])
        except TelegramApiError as exc:
            logging.error("Falha ao consultar getUpdates: %s", exc)
            time.sleep(10)
            continue
        except requests.RequestException as exc:
            logging.error("Falha de rede ao consultar getUpdates: %s", exc.__class__.__name__)
            time.sleep(10)
            continue

        for update in updates:
            offset = int(update["update_id"]) + 1
            message = update.get("message") or update.get("edited_message") or {}
            chat = message.get("chat") or {}
            chat_id = str(chat.get("id", "")).strip()
            text_raw = str(message.get("text", "")).strip()
            text = text_raw.lower()
            if not chat_id or not text:
                continue

            if text.startswith("/start"):
                save_subscriber(chat_id)
                reply(
                    token,
                    chat_id,
                    (
                        "Cadastro feito. Este chat recebera os cronogramas diarios.\n\n"
                        "Comandos: /id, /hoje, /ingles, /gramatica, /biblia, /ia sua pergunta, /ia_status, /cronograma."
                    ),
                )
            elif text.startswith("/ajuda") or text.startswith("/help"):
                reply(
                    token,
                    chat_id,
                    "Comandos: /id, /hoje, /amanha, /ingles, /gramatica, /biblia, /ia sua pergunta, /ia_status, /cronograma.",
                )
            elif text.startswith("/id"):
                reply(token, chat_id, f"Seu chat_id e: {chat_id}")
            elif text.startswith("/hoje"):
                today = datetime.now(timezone).date()
                lesson = lesson_for_date(lessons, start_date, today)
                if lesson:
                    for chunk in split_message(format_lesson(lesson, today)):
                        reply(token, chat_id, chunk)
                else:
                    reply(token, chat_id, "Nao ha aula programada para hoje.")
            elif text.startswith("/amanha"):
                tomorrow = datetime.now(timezone).date() + timedelta(days=1)
                lesson = lesson_for_date(lessons, start_date, tomorrow)
                if lesson:
                    for chunk in split_message(format_lesson(lesson, tomorrow)):
                        reply(token, chat_id, chunk)
                else:
                    reply(token, chat_id, "Nao ha aula programada para amanha.")
            elif text.startswith("/ingles"):
                today = datetime.now(timezone).date()
                lesson = weekday_lesson_for_date(english_lessons, today)
                if lesson:
                    for chunk in split_message(format_english_lesson(lesson, today)):
                        reply(token, chat_id, chunk)
                else:
                    reply(token, chat_id, "Nao ha aula de ingles programada para hoje.")
            elif text.startswith("/gramatica"):
                today = datetime.now(timezone).date()
                lesson = weekday_lesson_for_date(grammar_lessons, today)
                if lesson:
                    for chunk in split_message(format_grammar_lesson(lesson, today)):
                        reply(token, chat_id, chunk)
                else:
                    reply(token, chat_id, "Nao ha aula de gramatica programada para hoje.")
            elif text.startswith("/biblia"):
                today = datetime.now(timezone).date()
                lesson = sequential_lesson_for_date(bible_lessons, bible_start_date, today)
                if not lesson:
                    reply(token, chat_id, "Nao ha resumo biblico programado para hoje.")
                    continue

                try:
                    body = enhance_bible_summary_with_ai(lesson)
                except (requests.RequestException, DeepSeekApiError, GroqApiError, KeyError, IndexError) as exc:
                    logging.error("Falha ao usar IA no comando /biblia: %s", exc)
                    body = lesson.body

                for chunk in split_message(format_bible_lesson(lesson, today, body)):
                    reply(token, chat_id, chunk)
            elif text.startswith("/ia_status"):
                provider = active_ai_provider()
                if provider == "deepseek":
                    reply(token, chat_id, f"DeepSeek configurada. Modelo atual: {os.getenv('DEEP_MODEL', 'deepseek-v4-flash')}.")
                elif provider == "groq":
                    reply(token, chat_id, f"Groq configurada. Modelo atual: {os.getenv('GROQ_MODEL', 'llama-3.1-8b-instant')}.")
                else:
                    reply(token, chat_id, "IA nao configurada. Adicione DEEP_API_KEY ou GROQ_API_KEY nas variaveis do Railway.")
            elif text.startswith("/ia"):
                question = text_raw[3:].strip()
                if not question:
                    reply(token, chat_id, "Use assim: /ia escreva sua pergunta aqui.")
                    continue

                try:
                    answer = ask_ai(question)
                except (requests.RequestException, DeepSeekApiError, GroqApiError, KeyError, IndexError) as exc:
                    logging.error("Falha ao responder /ia: %s", exc)
                    reply(token, chat_id, ai_error_message(exc))
                    continue

                for chunk in split_message(answer):
                    reply(token, chat_id, chunk)
            elif text.startswith("/cronograma"):
                reply(
                    token,
                    chat_id,
                    f"Cronograma carregado com {len(lessons)} aulas. Inicio configurado: {start_date:%d/%m/%Y}.",
                )


def build_scheduler(
    token: str,
    lessons: list[Lesson],
    start_date: date,
    timezone: ZoneInfo,
    hour: int,
    minute: int,
) -> BlockingScheduler:
    scheduler = BlockingScheduler(timezone=timezone)
    trigger = CronTrigger(day_of_week="mon-fri", hour=hour, minute=minute, timezone=timezone)

    scheduler.add_job(
        lambda: send_lesson_to_subscribers(
            token=token,
            lessons=lessons,
            start_date=start_date,
            target_date=datetime.now(timezone).date(),
        ),
        trigger=trigger,
        id="daily_study_lesson",
        replace_existing=True,
        misfire_grace_time=900,
        coalesce=True,
    )
    return scheduler


def add_english_scheduler_job(
    scheduler: BlockingScheduler,
    token: str,
    lessons: dict[int, Lesson],
    timezone: ZoneInfo,
    hour: int,
    minute: int,
) -> None:
    trigger = CronTrigger(day_of_week="mon-fri", hour=hour, minute=minute, timezone=timezone)
    scheduler.add_job(
        lambda: send_weekday_lesson_to_subscribers(
            token=token,
            lessons=lessons,
            target_date=datetime.now(timezone).date(),
        ),
        trigger=trigger,
        id="daily_english_lesson",
        replace_existing=True,
        misfire_grace_time=900,
        coalesce=True,
    )


def add_grammar_scheduler_job(
    scheduler: BlockingScheduler,
    token: str,
    lessons: dict[int, Lesson],
    timezone: ZoneInfo,
    hour: int,
    minute: int,
) -> None:
    trigger = CronTrigger(day_of_week="mon-fri", hour=hour, minute=minute, timezone=timezone)
    scheduler.add_job(
        lambda: send_grammar_lesson_to_subscribers(
            token=token,
            lessons=lessons,
            target_date=datetime.now(timezone).date(),
        ),
        trigger=trigger,
        id="daily_grammar_lesson",
        replace_existing=True,
        misfire_grace_time=900,
        coalesce=True,
    )


def add_bible_scheduler_job(
    scheduler: BlockingScheduler,
    token: str,
    lessons: list[Lesson],
    start_date: date,
    timezone: ZoneInfo,
    hour: int,
    minute: int,
) -> None:
    trigger = CronTrigger(hour=hour, minute=minute, timezone=timezone)
    scheduler.add_job(
        lambda: send_bible_lesson_to_subscribers(
            token=token,
            lessons=lessons,
            start_date=start_date,
            target_date=datetime.now(timezone).date(),
        ),
        trigger=trigger,
        id="daily_bible_lesson",
        replace_existing=True,
        misfire_grace_time=900,
        coalesce=True,
    )


def dry_run(target_date: date) -> int:
    load_dotenv()
    lessons = parse_schedule(schedule_path())
    start_date = read_start_date()
    lesson = lesson_for_date(lessons, start_date, target_date)
    if not lesson:
        print(f"Nenhuma aula para {target_date.isoformat()}.")
        return 0

    print(format_lesson(lesson, target_date))
    return 0


def english_dry_run(target_date: date) -> int:
    load_dotenv()
    lessons = parse_weekday_schedule(english_schedule_path())
    lesson = weekday_lesson_for_date(lessons, target_date)
    if not lesson:
        print(f"Nenhuma aula de ingles para {target_date.isoformat()}.")
        return 0

    print(format_english_lesson(lesson, target_date))
    return 0


def grammar_dry_run(target_date: date) -> int:
    load_dotenv()
    lessons = parse_weekday_schedule(grammar_schedule_path())
    lesson = weekday_lesson_for_date(lessons, target_date)
    if not lesson:
        print(f"Nenhuma aula de gramatica para {target_date.isoformat()}.")
        return 0

    print(format_grammar_lesson(lesson, target_date))
    return 0


def bible_dry_run(target_date: date) -> int:
    load_dotenv()
    lessons = parse_bible_schedule(bible_schedule_path())
    start_date = parse_date(os.getenv("BIBLE_START_DATE", os.getenv("SCHEDULE_START_DATE", "")).strip())
    lesson = sequential_lesson_for_date(lessons, start_date, target_date)
    if not lesson:
        print(f"Nenhum resumo biblico para {target_date.isoformat()}.")
        return 0

    print(format_bible_lesson(lesson, target_date, lesson.body))
    return 0


def main() -> int:
    load_dotenv()
    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO").upper(),
        format="%(asctime)s %(levelname)s %(message)s",
        stream=sys.stdout,
        force=True,
    )

    timezone = ZoneInfo(os.getenv("TIMEZONE", "America/Sao_Paulo"))
    hour = int(os.getenv("SEND_HOUR", "9"))
    minute = int(os.getenv("SEND_MINUTE", "40"))
    english_hour = int(os.getenv("ENGLISH_SEND_HOUR", "19"))
    english_minute = int(os.getenv("ENGLISH_SEND_MINUTE", "0"))
    grammar_hour = int(os.getenv("GRAMMAR_SEND_HOUR", "18"))
    grammar_minute = int(os.getenv("GRAMMAR_SEND_MINUTE", "0"))
    grammar_enabled = parse_bool(os.getenv("GRAMMAR_ENABLED", "false"))
    bible_hour = int(os.getenv("BIBLE_SEND_HOUR", "14"))
    bible_minute = int(os.getenv("BIBLE_SEND_MINUTE", "0"))
    enable_polling = parse_bool(os.getenv("ENABLE_POLLING", "false"))
    send_test_on_start = parse_bool(os.getenv("SEND_TEST_ON_START", "false"))
    token = read_token()
    start_date = read_start_date()
    lessons = parse_schedule(schedule_path())
    english_lessons = parse_weekday_schedule(english_schedule_path())
    grammar_lessons = parse_weekday_schedule(grammar_schedule_path())
    bible_path = bible_schedule_path()
    bible_enabled = parse_bool(os.getenv("BIBLE_ENABLED", ""), default=bible_path.exists())
    bible_lessons: list[Lesson] = []
    bible_start_date = parse_date(os.getenv("BIBLE_START_DATE", start_date.isoformat()).strip())

    if not lessons:
        raise ConfigError("Nenhuma aula encontrada no cronograma.")
    if len(english_lessons) < 5:
        raise ConfigError("O cronograma de ingles precisa ter conteudo de segunda a sexta.")
    if len(grammar_lessons) < 5:
        raise ConfigError("O cronograma de gramatica precisa ter conteudo de segunda a sexta.")
    if bible_enabled:
        bible_lessons = parse_bible_schedule(bible_path)
        if not bible_lessons:
            raise ConfigError("O cronograma biblico precisa ter pelo menos um capitulo.")

    if enable_polling:
        polling_thread = threading.Thread(
            target=polling_loop,
            args=(token, lessons, start_date, english_lessons, grammar_lessons, bible_lessons, bible_start_date, timezone),
            daemon=True,
        )
        polling_thread.start()
    else:
        logging.info("Polling do Telegram desativado. Use ENABLE_POLLING=true para comandos como /id.")

    if send_test_on_start:
        subscribers = load_subscribers()
        if subscribers:
            test_message = (
                "Teste do BetEstudo: bot online e pronto para enviar o cronograma diario "
                f"as {hour:02d}:{minute:02d}."
            )
            for chat_id in subscribers:
                try:
                    send_telegram_message(token, chat_id, test_message)
                except (requests.RequestException, TelegramApiError) as exc:
                    logging.error("Falha ao enviar teste para chat_id=%s: %s", chat_id, exc)
                    continue
                logging.info("Mensagem de teste enviada para chat_id=%s.", chat_id)
        else:
            logging.warning("SEND_TEST_ON_START ativo, mas nenhum TELEGRAM_CHAT_IDS foi configurado.")

    scheduler = build_scheduler(token, lessons, start_date, timezone, hour, minute)
    add_english_scheduler_job(scheduler, token, english_lessons, timezone, english_hour, english_minute)
    if grammar_enabled:
        add_grammar_scheduler_job(scheduler, token, grammar_lessons, timezone, grammar_hour, grammar_minute)
    if bible_enabled:
        add_bible_scheduler_job(
            scheduler,
            token,
            bible_lessons,
            bible_start_date,
            timezone,
            bible_hour,
            bible_minute,
        )
    logging.info(
        "Bot iniciado com %s aulas. Disparo: seg-sex %02d:%02d (%s).",
        len(lessons),
        hour,
        minute,
        timezone.key,
    )
    logging.info(
        "Cronograma de ingles iniciado com %s aulas. Disparo: seg-sex %02d:%02d (%s).",
        len(english_lessons),
        english_hour,
        english_minute,
        timezone.key,
    )
    if grammar_enabled:
        logging.info(
            "Cronograma de gramatica iniciado com %s aulas. Disparo: seg-sex %02d:%02d (%s).",
            len(grammar_lessons),
            grammar_hour,
            grammar_minute,
            timezone.key,
        )
    else:
        logging.info("Cronograma de gramatica carregado com %s aulas. Envio automatico desativado.", len(grammar_lessons))
    if bible_enabled:
        logging.info(
            "Cronograma biblico iniciado com %s capitulos. Disparo: diario %02d:%02d (%s).",
            len(bible_lessons),
            bible_hour,
            bible_minute,
            timezone.key,
        )
    else:
        logging.info("Cronograma biblico desativado. Configure BIBLE_ENABLED=true quando o arquivo estiver pronto.")
    scheduler.start()
    return 0


if __name__ == "__main__":
    configure_stdout()
    parser = argparse.ArgumentParser(description="Bot Telegram do cronograma de estudos.")
    parser.add_argument("--dry-run", metavar="YYYY-MM-DD", help="Mostra a aula calculada para a data.")
    parser.add_argument("--english-dry-run", metavar="YYYY-MM-DD", help="Mostra a aula de ingles para a data.")
    parser.add_argument("--grammar-dry-run", metavar="YYYY-MM-DD", help="Mostra a aula de gramatica para a data.")
    parser.add_argument("--bible-dry-run", metavar="YYYY-MM-DD", help="Mostra o resumo biblico para a data.")
    args = parser.parse_args()

    try:
        if args.bible_dry_run:
            raise SystemExit(bible_dry_run(parse_date(args.bible_dry_run)))
        if args.grammar_dry_run:
            raise SystemExit(grammar_dry_run(parse_date(args.grammar_dry_run)))
        if args.english_dry_run:
            raise SystemExit(english_dry_run(parse_date(args.english_dry_run)))
        if args.dry_run:
            raise SystemExit(dry_run(parse_date(args.dry_run)))
        raise SystemExit(main())
    except ConfigError as exc:
        print(f"Erro de configuracao: {exc}", file=sys.stderr)
        raise SystemExit(2)
