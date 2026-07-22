# Notas de Backend e Deploy

Documento operacional do projeto BetEstudo. Nao salvar tokens, senhas ou API keys reais neste arquivo.

Ultima revisao: `2026-07-22`.

## Estado atual

Backend ativo: Cloudflare Workers.

- Worker: `betestudo`
- URL publica: `https://betestudo.betestudo.workers.dev`
- Conta Cloudflare: login via GitHub `tecnicorikardo`
- Email mostrado pelo Wrangler: `tecnicorikardo@gmail.com`
- Account ID Cloudflare: `a748550556d8b4bfd8c0635578773242`
- Repositorio GitHub: `https://github.com/tecnicorikardo/betEstudo`
- Branch usada em producao: `main`
- Bot Telegram: `@BetEstudoBot`
- Chat privado principal: `5449614637`
- IA principal: DeepSeek via secret `DEEP_API_KEY`
- Conta DeepSeek: `rikardomartinssantos@gmail.com`
- IA fallback/opcional: Groq via secret `GROQ_API_KEY`

O Telegram esta ligado ao Worker por webhook:

```text
https://betestudo.betestudo.workers.dev/telegram
```

## O que esta em uso

- Cloudflare Workers: hospeda o bot e executa os horarios automaticos.
- Cloudflare Cron Triggers: dispara os envios automaticos.
- Telegram Bot API: recebe comandos por webhook e envia mensagens.
- GitHub raw: fornece os arquivos Markdown de conteudo.
- DeepSeek API: responde `/ia` e melhora o resumo biblico quando configurada.
- Node.js/Wrangler: ferramenta de deploy do Worker.

## O que ja foi usado ou investigado

- Railway: foi usado como backend Python, mas o trial expirou e o servico ficou offline.
- Render: foi investigado por API, mas nao era o backend em uso do bot.
- Groq: foi configurado/investigado como IA. Atualmente fica como fallback caso `GROQ_API_KEY` exista.
- Python `bot.py`: continua no repositorio como fallback para Railway/outro worker 24/7, mas nao e o backend ativo.

## Rotina de envios

- TI: segunda a sexta, `09:40`, arquivo `cronograma_ti_20_semanas_detalhado.md`.
- Biblia: todos os dias, `14:00`, arquivo `resumo_novo_testamento.md`.
- Ingles: segunda a sexta, `19:00`, arquivo `Guia Completo_ Frases do Cotidiano Americano.md`.
- Gramatica: disponivel por comando `/gramatica`, arquivo `gramatica.md`.

No Cloudflare, os horarios estao em UTC no arquivo `wrangler.toml`:

```text
40 12 * * 1-5 = TI, segunda a sexta, 09:40 em Sao Paulo
0 17 * * *    = Biblia, todos os dias, 14:00 em Sao Paulo
0 22 * * 1-5  = Ingles, segunda a sexta, 19:00 em Sao Paulo
```

## Secrets atuais no Cloudflare

Esses nomes devem existir no Worker. Os valores reais nao devem ser documentados.

Obrigatorios:

```env
TELEGRAM_BOT_TOKEN=
DEEP_API_KEY=
```

Opcionais:

```env
GROQ_API_KEY=
TELEGRAM_WEBHOOK_SECRET=
```

## Variaveis atuais no Cloudflare

Configuradas em `wrangler.toml`:

```env
TELEGRAM_CHAT_IDS=5449614637
SCHEDULE_START_DATE=2026-06-01
BIBLE_START_DATE=2026-06-01
TIMEZONE=America/Sao_Paulo
RAW_BASE_URL=https://raw.githubusercontent.com/tecnicorikardo/betEstudo/main/
SCHEDULE_FILE=cronograma_ti_20_semanas_detalhado.md
ENGLISH_SCHEDULE_FILE=Guia Completo_ Frases do Cotidiano Americano.md
GRAMMAR_SCHEDULE_FILE=gramatica.md
BIBLE_SCHEDULE_FILE=resumo_novo_testamento.md
DEEP_MODEL=deepseek-v4-flash
DEEP_BASE_URL=https://api.deepseek.com
DEEP_THINKING=disabled
GROQ_MODEL=llama-3.1-8b-instant
```

## Variaveis Railway antigas

Mantidas apenas para referencia da versao Python antiga.

```env
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_IDS=5449614637
SCHEDULE_START_DATE=2026-06-01
TIMEZONE=America/Sao_Paulo
SEND_HOUR=9
SEND_MINUTE=40
ENGLISH_SEND_HOUR=19
ENGLISH_SEND_MINUTE=0
GRAMMAR_SCHEDULE_FILE=gramatica.md
GRAMMAR_ENABLED=false
GRAMMAR_SEND_HOUR=18
GRAMMAR_SEND_MINUTE=0
BIBLE_ENABLED=true
BIBLE_SCHEDULE_FILE=resumo_novo_testamento.md
BIBLE_SCHEDULE_URL=https://raw.githubusercontent.com/tecnicorikardo/betEstudo/main/resumo_novo_testamento.md
BIBLE_START_DATE=2026-06-01
BIBLE_SEND_HOUR=14
BIBLE_SEND_MINUTE=0
GROQ_API_KEY=
GROQ_MODEL=llama-3.1-8b-instant
DEEP_API_KEY=
DEEP_MODEL=deepseek-v4-flash
DEEP_BASE_URL=https://api.deepseek.com
DEEP_THINKING=disabled
ENABLE_POLLING=true
SEND_TEST_ON_START=false
```

Opcionais:

```env
GROQ_TEMPERATURE=0.4
GROQ_MAX_TOKENS=700
DEEP_TEMPERATURE=0.4
DEEP_MAX_TOKENS=700
LOG_LEVEL=INFO
```

## Comandos Telegram

- `/start`: cadastra o chat.
- `/id`: mostra o chat_id.
- `/hoje`: envia a aula de TI de hoje.
- `/amanha`: envia a aula de TI de amanha.
- `/ingles`: envia o conteudo de ingles de hoje.
- `/gramatica`: envia a aula de gramatica inglesa de hoje.
- `/biblia`: envia o resumo biblico de hoje usando DeepSeek ou Groq quando disponivel.
- `/ia sua pergunta`: responde usando DeepSeek ou Groq.
- `/ia_status`: mostra qual IA foi configurada no ambiente.
- `/cronograma`: mostra status do cronograma de TI.
- `/ajuda`: lista comandos.

## Cuidados

- Nunca commitar `.env`, `token telegram.txt`, `subscribers.json`, tokens ou API keys reais.
- No Cloudflare, salvar `TELEGRAM_BOT_TOKEN`, `DEEP_API_KEY`, `GROQ_API_KEY` e `TELEGRAM_WEBHOOK_SECRET` como secrets.
- Depois de testar com `SEND_TEST_ON_START=true`, voltar para `false`.
- Manter apenas um webhook ativo do Telegram para este bot.
- Na versao Python antiga, manter apenas uma instancia com `ENABLE_POLLING=true`; mais de uma instancia pode gerar conflito `409 Conflict` no Telegram.
- Se o Railway nao encontrar `resumo_novo_testamento.md`, o bot usa `BIBLE_SCHEDULE_URL` como fallback.
- Push para GitHub deve ser feito manualmente pelo usuario.

## Deploy Cloudflare Workers

Deploy recomendado e ativo.

1. Instalar dependencias: `npm install`.
2. Testar parsers: `npm test`.
3. Fazer login: `npx wrangler login`.
4. Criar secrets:

```bash
npx wrangler secret put TELEGRAM_BOT_TOKEN
npx wrangler secret put DEEP_API_KEY
npx wrangler secret put GROQ_API_KEY
npx wrangler secret put TELEGRAM_WEBHOOK_SECRET
```

5. Publicar: `npx wrangler deploy`.
6. Configurar o webhook do Telegram:

```bash
TOKEN="$(cat 'token telegram.txt' | tr -d '\r\n')"
curl -s "https://api.telegram.org/bot$TOKEN/setWebhook?url=https://betestudo.betestudo.workers.dev/telegram"
```

## Deploy Railway antigo

1. Fazer commit local das alteracoes.
2. Fazer push manual para `main`.
3. No Railway, usar deploy manual/latest commit se o deploy automatico nao iniciar.
4. Conferir logs esperados:

```text
Bot iniciado com 100 aulas. Disparo: seg-sex 09:40 (America/Sao_Paulo).
Cronograma biblico iniciado com 260 capitulos. Disparo: diario 14:00 (America/Sao_Paulo).
Cronograma de ingles iniciado com 5 aulas. Disparo: seg-sex 19:00 (America/Sao_Paulo).
Scheduler started
```
