const WEEKDAY_NAMES = [
  "Segunda-feira",
  "Terca-feira",
  "Quarta-feira",
  "Quinta-feira",
  "Sexta-feira"
];

const WEEKDAY_KEYS = new Map([
  ["segunda-feira", 0],
  ["segunda", 0],
  ["terca-feira", 1],
  ["terça-feira", 1],
  ["terca", 1],
  ["terça", 1],
  ["quarta-feira", 2],
  ["quarta", 2],
  ["quinta-feira", 3],
  ["quinta", 3],
  ["sexta-feira", 4],
  ["sexta", 4]
]);

const CRON_TI = "40 12 * * 1-5";
const CRON_BIBLE = "0 17 * * *";
const CRON_ENGLISH = "0 22 * * 1-5";

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (request.method === "GET") {
      return json({
        ok: true,
        service: "BetEstudo Cloudflare Worker",
        commands: ["/id", "/hoje", "/amanha", "/ingles", "/gramatica", "/biblia", "/ia_status", "/ia sua pergunta"]
      });
    }

    if (request.method === "POST" && isTelegramWebhook(url, env)) {
      const update = await request.json();
      ctx.waitUntil(handleTelegramUpdate(update, env));
      return json({ ok: true });
    }

    return new Response("Not found", { status: 404 });
  },

  async scheduled(controller, env, ctx) {
    ctx.waitUntil(handleCron(controller.cron, env));
  }
};

async function handleCron(cron, env) {
  const today = localDateParts(new Date(), env.TIMEZONE || "America/Sao_Paulo");

  if (cron === CRON_TI) {
    const lessons = parseTiSchedule(await fetchText(env, env.SCHEDULE_FILE));
    const lesson = lessonForBusinessDate(lessons, env.SCHEDULE_START_DATE, today.date);
    if (lesson) await sendToSubscribers(env, formatTiLesson(lesson, today.date));
    return;
  }

  if (cron === CRON_BIBLE) {
    const lessons = parseBibleSchedule(await fetchText(env, env.BIBLE_SCHEDULE_FILE));
    const lesson = sequentialLessonForDate(lessons, env.BIBLE_START_DATE || env.SCHEDULE_START_DATE, today.date);
    if (!lesson) return;

    let body = lesson.body;
    try {
      body = await enhanceBibleSummaryWithAi(env, lesson);
    } catch (error) {
      console.log(`AI failed for bible cron: ${safeError(error)}. Sending original summary.`);
    }
    await sendToSubscribers(env, formatBibleLesson(lesson, today.date, body));
    return;
  }

  if (cron === CRON_ENGLISH) {
    const lessons = parseWeekdaySchedule(await fetchText(env, env.ENGLISH_SCHEDULE_FILE));
    const lesson = lessons.get(today.weekday);
    if (lesson) await sendToSubscribers(env, formatEnglishLesson(lesson, today.date));
  }
}

async function handleTelegramUpdate(update, env) {
  const message = update.message || update.edited_message;
  const chatId = message?.chat?.id?.toString();
  const textRaw = message?.text?.trim();
  if (!chatId || !textRaw) return;

  const text = textRaw.toLowerCase();
  const today = localDateParts(new Date(), env.TIMEZONE || "America/Sao_Paulo");

  if (text.startsWith("/start")) {
    await reply(env, chatId, "Cadastro feito. Comandos: /id, /hoje, /ingles, /gramatica, /biblia, /ia sua pergunta, /ia_status.");
    return;
  }

  if (text.startsWith("/ajuda") || text.startsWith("/help")) {
    await reply(env, chatId, "Comandos: /id, /hoje, /amanha, /ingles, /gramatica, /biblia, /ia sua pergunta, /ia_status.");
    return;
  }

  if (text.startsWith("/id")) {
    await reply(env, chatId, `Seu chat_id e: ${chatId}`);
    return;
  }

  if (text.startsWith("/hoje") || text.startsWith("/amanha")) {
    const target = text.startsWith("/amanha") ? addDays(today.date, 1) : today.date;
    const lessons = parseTiSchedule(await fetchText(env, env.SCHEDULE_FILE));
    const lesson = lessonForBusinessDate(lessons, env.SCHEDULE_START_DATE, target);
    await replyChunks(env, chatId, lesson ? formatTiLesson(lesson, target) : "Nao ha aula de TI programada para esta data.");
    return;
  }

  if (text.startsWith("/ingles")) {
    const lessons = parseWeekdaySchedule(await fetchText(env, env.ENGLISH_SCHEDULE_FILE));
    const lesson = lessons.get(today.weekday);
    await replyChunks(env, chatId, lesson ? formatEnglishLesson(lesson, today.date) : "Nao ha aula de ingles programada para hoje.");
    return;
  }

  if (text.startsWith("/gramatica")) {
    const lessons = parseWeekdaySchedule(await fetchText(env, env.GRAMMAR_SCHEDULE_FILE));
    const lesson = lessons.get(today.weekday);
    await replyChunks(env, chatId, lesson ? formatGrammarLesson(lesson, today.date) : "Nao ha aula de gramatica programada para hoje.");
    return;
  }

  if (text.startsWith("/biblia")) {
    const lessons = parseBibleSchedule(await fetchText(env, env.BIBLE_SCHEDULE_FILE));
    const lesson = sequentialLessonForDate(lessons, env.BIBLE_START_DATE || env.SCHEDULE_START_DATE, today.date);
    if (!lesson) {
      await reply(env, chatId, "Nao ha resumo biblico programado para hoje.");
      return;
    }

    let body = lesson.body;
    try {
      body = await enhanceBibleSummaryWithAi(env, lesson);
    } catch (error) {
      console.log(`AI failed for /biblia: ${safeError(error)}. Sending original summary.`);
    }
    await replyChunks(env, chatId, formatBibleLesson(lesson, today.date, body));
    return;
  }

  if (text.startsWith("/ia_status")) {
    const provider = activeAiProvider(env);
    if (provider === "deepseek") {
      await reply(env, chatId, `DeepSeek configurada. Modelo atual: ${env.DEEP_MODEL || "deepseek-v4-flash"}.`);
    } else if (provider === "groq") {
      await reply(env, chatId, `Groq configurada. Modelo atual: ${env.GROQ_MODEL || "llama-3.1-8b-instant"}.`);
    } else {
      await reply(env, chatId, "IA nao configurada. Adicione DEEP_API_KEY ou GROQ_API_KEY nas variaveis do Cloudflare Worker.");
    }
    return;
  }

  if (text.startsWith("/ia")) {
    const question = textRaw.slice(3).trim();
    if (!question) {
      await reply(env, chatId, "Use assim: /ia escreva sua pergunta aqui.");
      return;
    }

    try {
      const answer = await askAi(env, question);
      await replyChunks(env, chatId, answer);
    } catch (error) {
      await reply(env, chatId, aiErrorMessage(error));
    }
  }
}

function isTelegramWebhook(url, env) {
  const secret = env.TELEGRAM_WEBHOOK_SECRET;
  if (secret) return url.pathname === `/telegram/${secret}`;
  return url.pathname === "/telegram";
}

async function fetchText(env, filename) {
  const baseUrl = env.RAW_BASE_URL || "https://raw.githubusercontent.com/tecnicorikardo/betEstudo/main/";
  const response = await fetch(new URL(encodeURI(filename), baseUrl).toString());
  if (!response.ok) throw new Error(`Failed to fetch ${filename}: HTTP ${response.status}`);
  return response.text();
}

function parseTiSchedule(markdown) {
  const lessons = [];
  let currentModule = "";
  let currentWeek = 0;
  let currentWeekTitle = "";
  let current = null;
  let body = [];

  const flush = () => {
    if (!current) return;
    lessons.push({ ...current, body: body.join("\n").trim() });
    current = null;
    body = [];
  };

  for (const line of markdown.split(/\r?\n/)) {
    const moduleMatch = line.match(/^##\s+(?!#)(.+?)\s*$/);
    if (moduleMatch) {
      flush();
      currentModule = moduleMatch[1].trim();
      continue;
    }

    const weekMatch = line.match(/^###\s+Semana\s+(\d+)\b\s*(?:[-–]\s*)?(.*)$/i);
    if (weekMatch) {
      flush();
      currentWeek = Number(weekMatch[1]);
      currentWeekTitle = weekMatch[2].trim();
      continue;
    }

    const lessonMatch = line.match(/^####\s+([^:]+):\s*(.+?)\s*$/);
    if (lessonMatch) {
      const weekday = WEEKDAY_KEYS.get(normalizeText(lessonMatch[1]));
      if (weekday === undefined) continue;
      flush();
      current = {
        module: currentModule,
        week: currentWeek,
        weekTitle: currentWeekTitle,
        weekday,
        weekdayName: WEEKDAY_NAMES[weekday],
        title: lessonMatch[2].trim()
      };
      continue;
    }

    if (current) body.push(line);
  }

  flush();
  return lessons.sort((a, b) => a.week - b.week || a.weekday - b.weekday);
}

function parseWeekdaySchedule(markdown) {
  const lessons = new Map();
  let documentTitle = "Cronograma";
  let current = null;
  let body = [];

  const flush = () => {
    if (!current) return;
    lessons.set(current.weekday, { ...current, body: body.join("\n").trim() });
    current = null;
    body = [];
  };

  for (const line of markdown.split(/\r?\n/)) {
    const titleMatch = line.match(/^#\s+(?!#)(.+?)\s*$/);
    if (titleMatch) {
      documentTitle = titleMatch[1].trim();
      continue;
    }

    const sectionMatch = line.match(/^#{2,6}\s+(?:[^\wÀ-ÿ]+)?\**(segunda-feira|terca-feira|terça-feira|quarta-feira|quinta-feira|sexta-feira)\**\s*(?::|[-–])\s*\**(.+?)\**\s*$/i);
    if (sectionMatch) {
      const weekday = WEEKDAY_KEYS.get(normalizeText(sectionMatch[1]));
      if (weekday === undefined) continue;
      flush();
      current = {
        module: documentTitle,
        weekday,
        weekdayName: WEEKDAY_NAMES[weekday],
        title: sectionMatch[2].trim().replace(/\*+$/g, "")
      };
      continue;
    }

    if (current) body.push(line);
  }

  flush();
  return lessons;
}

function parseBibleSchedule(markdown) {
  const lessons = [];
  let currentBook = "";
  const seen = new Set();

  const cleanCell = (value) => value.trim().replace(/^\*\*(.+?)\*\*$/u, "$1").trim();
  const addChapter = (title, body) => {
    const key = normalizeText(title);
    if (seen.has(key)) return;
    seen.add(key);
    lessons.push({ module: "Resumo do Novo Testamento", title, body: body.trim() });
  };

  for (const line of markdown.split(/\r?\n/)) {
    const bookMatch = line.match(/^#\s+(?!#)(.+?)\s*$/);
    if (bookMatch) {
      currentBook = bookMatch[1].trim();
      continue;
    }

    if (!currentBook || !line.trim().startsWith("|")) continue;

    const cells = line.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map(cleanCell);
    if (!cells.length || cells.every((cell) => /^:?-+:?$/.test(cell))) continue;
    const first = normalizeText(cells[0]);
    if (first === "capitulo" || first === "tema principal") continue;

    if (cells.length >= 3 && /^\d+$/.test(cells[0])) {
      addChapter(`${currentBook} ${cells[0]}`, `Tema principal: ${cells[1]}\n\nResumo: ${cells.slice(2).join(" | ")}`);
    } else if (cells.length >= 2 && cells[0] && cells[1]) {
      addChapter(`${currentBook} 1`, `Tema principal: ${cells[0]}\n\nResumo: ${cells.slice(1).join(" | ")}`);
    }
  }

  return lessons;
}

function lessonForBusinessDate(lessons, startDate, targetDate) {
  if (!startDate || targetDate < startDate) return null;
  const weekday = weekdayIndex(targetDate);
  if (weekday > 4) return null;
  const elapsedDays = daysBetween(startDate, targetDate);
  const lessonIndex = Math.floor(elapsedDays / 7) * 5 + weekday;
  return lessons[lessonIndex] || null;
}

function sequentialLessonForDate(lessons, startDate, targetDate) {
  if (!startDate || targetDate < startDate) return null;
  const lessonIndex = daysBetween(startDate, targetDate);
  return lessons[lessonIndex] || null;
}

function formatTiLesson(lesson, targetDate) {
  return [
    "Aula de hoje",
    `Data: ${formatBrDate(targetDate)}`,
    `Modulo: ${lesson.module}`,
    `Semana ${lesson.week}: ${lesson.weekTitle}`,
    `Dia: ${lesson.weekdayName}`,
    `Tema: ${lesson.title}`,
    "",
    "Conteudo:",
    lesson.body
  ].join("\n");
}

function formatEnglishLesson(lesson, targetDate) {
  return formatWeekdayLesson("Ingles de hoje", lesson, targetDate);
}

function formatGrammarLesson(lesson, targetDate) {
  return formatWeekdayLesson("Gramatica de ingles de hoje", lesson, targetDate);
}

function formatWeekdayLesson(label, lesson, targetDate) {
  return [
    label,
    `Data: ${formatBrDate(targetDate)}`,
    `Guia: ${lesson.module}`,
    `Dia: ${lesson.weekdayName}`,
    `Tema: ${lesson.title}`,
    "",
    "Conteudo:",
    lesson.body
  ].join("\n");
}

function formatBibleLesson(lesson, targetDate, body) {
  return [
    "Resumo biblico de hoje",
    `Data: ${formatBrDate(targetDate)}`,
    `Serie: ${lesson.module}`,
    `Capitulo: ${lesson.title}`,
    "",
    "Conteudo:",
    body || lesson.body
  ].join("\n");
}

async function enhanceBibleSummaryWithAi(env, lesson) {
  const prompt = [
    "Transforme o resumo abaixo em uma mensagem diaria para Telegram, em portugues do Brasil.",
    "Seja claro, respeitoso e fiel ao conteudo biblico.",
    "Organize em: 1) resumo do capitulo, 2) mensagem principal, 3) aplicacao pratica para hoje.",
    "Nao invente versiculos nem fatos que nao estejam no texto.",
    "Mantenha entre 120 e 220 palavras.",
    "",
    `Capitulo: ${lesson.title}`,
    "",
    `Resumo base:\n${lesson.body}`
  ].join("\n");

  return aiChatCompletion(env, [
    { role: "system", content: "Voce e um assistente de estudos biblicos. Responda com linguagem simples, devocional leve e foco em compreensao do Novo Testamento." },
    { role: "user", content: prompt }
  ]);
}

async function askAi(env, question) {
  return aiChatCompletion(env, [
    { role: "system", content: "Voce e o assistente do bot BetEstudo. Responda em portugues do Brasil, com clareza, objetividade e tom respeitoso. Ajude em estudos de TI, ingles e resumos biblicos quando solicitado." },
    { role: "user", content: question }
  ]);
}

function activeAiProvider(env) {
  if (env.DEEP_API_KEY || env.DEEPSEEK_API_KEY) return "deepseek";
  if (env.GROQ_API_KEY) return "groq";
  return null;
}

async function aiChatCompletion(env, messages) {
  const provider = activeAiProvider(env);
  if (provider === "deepseek") return deepseekChatCompletion(env, messages);
  if (provider === "groq") return groqChatCompletion(env, messages);
  throw new Error("Nenhuma IA configurada. Configure DEEP_API_KEY ou GROQ_API_KEY.");
}

async function deepseekChatCompletion(env, messages) {
  const apiKey = env.DEEP_API_KEY || env.DEEPSEEK_API_KEY;
  const baseUrl = (env.DEEP_BASE_URL || "https://api.deepseek.com").replace(/\/+$/g, "");
  const response = await fetch(`${baseUrl}/chat/completions`, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${apiKey}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: env.DEEP_MODEL || "deepseek-v4-flash",
      messages,
      thinking: { type: env.DEEP_THINKING || "disabled" },
      temperature: Number(env.DEEP_TEMPERATURE || env.GROQ_TEMPERATURE || "0.4"),
      max_tokens: Number(env.DEEP_MAX_TOKENS || env.GROQ_MAX_TOKENS || "700")
    })
  });
  return parseAiResponse(response, "DeepSeek");
}

async function groqChatCompletion(env, messages) {
  const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${env.GROQ_API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: env.GROQ_MODEL || "llama-3.1-8b-instant",
      messages,
      temperature: Number(env.GROQ_TEMPERATURE || "0.4"),
      max_tokens: Number(env.GROQ_MAX_TOKENS || "700")
    })
  });
  return parseAiResponse(response, "Groq");
}

async function parseAiResponse(response, provider) {
  const payload = await response.json().catch(() => ({}));
  if (!response.ok) {
    const description = payload?.error?.message || response.statusText;
    throw new Error(`${provider} falhou: HTTP ${response.status} - ${description}`);
  }
  return payload.choices?.[0]?.message?.content?.trim() || "A IA nao retornou conteudo.";
}

function aiErrorMessage(error) {
  const message = safeError(error);
  if (message.includes("401") || message.includes("403")) {
    return "A IA recusou a chave configurada. Confira DEEP_API_KEY ou GROQ_API_KEY no Cloudflare Worker.";
  }
  if (message.includes("404") || message.toLowerCase().includes("model")) {
    return "A IA recusou o modelo configurado. Confira DEEP_MODEL ou GROQ_MODEL.";
  }
  if (message.includes("429")) {
    return "A IA bloqueou por limite de uso ou muitas requisicoes. Tente novamente em alguns minutos.";
  }
  return "Nao consegui responder com a IA agora. Confira as variaveis de IA no Cloudflare Worker.";
}

async function sendToSubscribers(env, text) {
  const chatIds = (env.TELEGRAM_CHAT_IDS || "").split(/[;,]/).map((item) => item.trim()).filter(Boolean);
  for (const chatId of chatIds) {
    await replyChunks(env, chatId, text);
  }
}

async function replyChunks(env, chatId, text) {
  for (const chunk of splitMessage(text)) {
    await reply(env, chatId, chunk);
  }
}

async function reply(env, chatId, text) {
  const response = await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      chat_id: chatId,
      text,
      disable_web_page_preview: true
    })
  });

  if (!response.ok) {
    const payload = await response.json().catch(() => ({}));
    console.log(`Telegram send failed: HTTP ${response.status} - ${payload.description || response.statusText}`);
  }
}

function splitMessage(text, limit = 3900) {
  if (text.length <= limit) return [text];
  const chunks = [];
  let remaining = text;

  while (remaining.length > limit) {
    let splitAt = remaining.lastIndexOf("\n\n", limit);
    if (splitAt < limit * 0.5) splitAt = remaining.lastIndexOf("\n", limit);
    if (splitAt < limit * 0.5) splitAt = limit;
    chunks.push(remaining.slice(0, splitAt).trim());
    remaining = remaining.slice(splitAt).trim();
  }

  if (remaining) chunks.push(remaining);
  return chunks.length === 1 ? chunks : chunks.map((chunk, index) => `Parte ${index + 1}/${chunks.length}\n\n${chunk}`);
}

function localDateParts(date, timezone) {
  const formatter = new Intl.DateTimeFormat("en-CA", {
    timeZone: timezone,
    year: "numeric",
    month: "2-digit",
    day: "2-digit"
  });
  const parts = Object.fromEntries(formatter.formatToParts(date).map((part) => [part.type, part.value]));
  const localDate = `${parts.year}-${parts.month}-${parts.day}`;
  return { date: localDate, weekday: weekdayIndex(localDate) };
}

function weekdayIndex(dateString) {
  const day = parseDateUtc(dateString).getUTCDay();
  return day === 0 ? 6 : day - 1;
}

function daysBetween(startDate, targetDate) {
  const start = parseDateUtc(startDate);
  const target = parseDateUtc(targetDate);
  return Math.floor((target - start) / 86400000);
}

function addDays(dateString, days) {
  const date = parseDateUtc(dateString);
  date.setUTCDate(date.getUTCDate() + days);
  return date.toISOString().slice(0, 10);
}

function parseDateUtc(dateString) {
  const [year, month, day] = dateString.split("-").map(Number);
  return new Date(Date.UTC(year, month - 1, day));
}

function formatBrDate(dateString) {
  const [year, month, day] = dateString.split("-");
  return `${day}/${month}/${year}`;
}

function normalizeText(value) {
  return value.trim().toLowerCase().normalize("NFD").replace(/\p{Diacritic}/gu, "");
}

function safeError(error) {
  return error instanceof Error ? error.message : String(error);
}

function json(payload, init = {}) {
  return new Response(JSON.stringify(payload), {
    ...init,
    headers: { "Content-Type": "application/json", ...(init.headers || {}) }
  });
}

export const __test = {
  parseBibleSchedule,
  parseTiSchedule,
  parseWeekdaySchedule,
  lessonForBusinessDate,
  sequentialLessonForDate
};
