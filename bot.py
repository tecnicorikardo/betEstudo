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
from typing import Iterable
from zoneinfo import ZoneInfo

import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parent
DEFAULT_SCHEDULE_FILE = ROOT_DIR / "cronograma_ti_20_semanas_detalhado.md"
LOCAL_TOKEN_FILE = ROOT_DIR / "token telegram.txt"
SUBSCRIBERS_FILE = ROOT_DIR / "subscribers.json"

MODULE_RE = re.compile(r"^##\s+(?!#)(.+?)\s*$")
WEEK_RE = re.compile(r"^###\s+Semana\s+(\d+)\b\s*(?:[-\u2013]\s*)?(.*)$")
LESSON_RE = re.compile(r"^####\s+([^:]+):\s*(.+?)\s*$")

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


def lesson_for_date(lessons: list[Lesson], start_date: date, target_date: date) -> Lesson | None:
    if target_date < start_date or target_date.weekday() > 4:
        return None

    elapsed_days = (target_date - start_date).days
    lesson_index = (elapsed_days // 7) * 5 + target_date.weekday()
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
    response.raise_for_status()


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
            send_telegram_message(token, chat_id, chunk)
            time.sleep(0.4)
        logging.info("Aula enviada para chat_id=%s.", chat_id)


def reply(token: str, chat_id: str, text: str) -> None:
    try:
        send_telegram_message(token, chat_id, text)
    except requests.RequestException:
        logging.exception("Falha ao responder chat_id=%s.", chat_id)


def polling_loop(token: str, lessons: list[Lesson], start_date: date, timezone: ZoneInfo) -> None:
    offset: int | None = None
    logging.info("Polling do Telegram iniciado.")

    while True:
        try:
            response = requests.get(
                telegram_api_url(token, "getUpdates"),
                params={"timeout": 30, "offset": offset},
                timeout=40,
            )
            response.raise_for_status()
            updates = response.json().get("result", [])
        except requests.RequestException:
            logging.exception("Falha ao consultar getUpdates.")
            time.sleep(10)
            continue

        for update in updates:
            offset = int(update["update_id"]) + 1
            message = update.get("message") or update.get("edited_message") or {}
            chat = message.get("chat") or {}
            chat_id = str(chat.get("id", "")).strip()
            text = str(message.get("text", "")).strip().lower()
            if not chat_id or not text:
                continue

            if text.startswith("/start"):
                save_subscriber(chat_id)
                reply(
                    token,
                    chat_id,
                    "Cadastro feito. Este chat recebera a materia diaria de segunda a sexta, as 09:40.",
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


def main() -> int:
    load_dotenv()
    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO").upper(),
        format="%(asctime)s %(levelname)s %(message)s",
    )

    timezone = ZoneInfo(os.getenv("TIMEZONE", "America/Sao_Paulo"))
    hour = int(os.getenv("SEND_HOUR", "9"))
    minute = int(os.getenv("SEND_MINUTE", "40"))
    token = read_token()
    start_date = read_start_date()
    lessons = parse_schedule(schedule_path())

    if not lessons:
        raise ConfigError("Nenhuma aula encontrada no cronograma.")

    polling_thread = threading.Thread(
        target=polling_loop,
        args=(token, lessons, start_date, timezone),
        daemon=True,
    )
    polling_thread.start()

    scheduler = build_scheduler(token, lessons, start_date, timezone, hour, minute)
    logging.info(
        "Bot iniciado com %s aulas. Disparo: seg-sex %02d:%02d (%s).",
        len(lessons),
        hour,
        minute,
        timezone.key,
    )
    scheduler.start()
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bot Telegram do cronograma de estudos.")
    parser.add_argument("--dry-run", metavar="YYYY-MM-DD", help="Mostra a aula calculada para a data.")
    args = parser.parse_args()

    try:
        if args.dry_run:
            raise SystemExit(dry_run(parse_date(args.dry_run)))
        raise SystemExit(main())
    except ConfigError as exc:
        print(f"Erro de configuracao: {exc}", file=sys.stderr)
        raise SystemExit(2)
