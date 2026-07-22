# Deploy no Cloudflare Workers

Este projeto pode rodar no Cloudflare Workers, sem processo 24/7. O Worker usa:

- Webhook do Telegram para comandos.
- Cron Triggers para os envios automaticos.
- Arquivos Markdown lidos do GitHub raw.

## Horarios

Cloudflare Cron usa UTC. Para `America/Sao_Paulo`:

- TI: `40 12 * * 1-5` = segunda a sexta, 09:40.
- Biblia: `0 17 * * *` = todos os dias, 14:00.
- Ingles: `0 22 * * 1-5` = segunda a sexta, 19:00.

Gramatica fica por comando `/gramatica`, porque este Worker ja usa tres cron triggers.

## Variaveis e secrets

Configure como secrets no Cloudflare:

```bash
npx wrangler secret put TELEGRAM_BOT_TOKEN
npx wrangler secret put DEEP_API_KEY
```

Opcionais:

```bash
npx wrangler secret put GROQ_API_KEY
npx wrangler secret put TELEGRAM_WEBHOOK_SECRET
```

As variaveis nao secretas ficam em `wrangler.toml`.

## Deploy

```bash
npm install
npm test
npx wrangler login
npx wrangler deploy
```

Depois do deploy, configure o webhook do Telegram:

```bash
curl "https://api.telegram.org/botSEU_TOKEN/setWebhook?url=https://betestudo.SEU_SUBDOMAIN.workers.dev/telegram"
```

Se configurar `TELEGRAM_WEBHOOK_SECRET`, use:

```bash
curl "https://api.telegram.org/botSEU_TOKEN/setWebhook?url=https://betestudo.SEU_SUBDOMAIN.workers.dev/telegram/SEU_SEGREDO"
```

## Comandos

- `/id`
- `/hoje`
- `/amanha`
- `/ingles`
- `/gramatica`
- `/biblia`
- `/ia_status`
- `/ia sua pergunta`

## Testes

```bash
npm test
node --check src/worker.js
```
