# Notas de Backend e Deploy

Documento operacional do projeto BetEstudo. Nao salvar tokens, senhas ou API keys reais neste arquivo.

## Contas e acessos

- Railway: `martinsantosric@gmail.com`
- Groq: `martinsantosric@gmail.com`
- DeepSeek: usar chave em `DEEP_API_KEY`
- GitHub: `tecnicorikardo`
- Repositorio: `https://github.com/tecnicorikardo/betEstudo`
- Bot Telegram: `@BetEstudoBot`
- Chat privado principal: `5449614637`

## Rotina de envios

- TI: segunda a sexta, `09:40`, arquivo `cronograma_ti_20_semanas_detalhado.md`.
- Biblia: todos os dias, `14:00`, arquivo `resumo_novo_testamento.md`.
- Ingles: segunda a sexta, `19:00`, arquivo `Guia Completo_ Frases do Cotidiano Americano.md`.
- Gramatica: disponivel por comando `/gramatica`, arquivo `gramatica.md`; envio automatico opcional.

## Variaveis Railway

Obrigatorias:

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
- Depois de testar com `SEND_TEST_ON_START=true`, voltar para `false`.
- Manter apenas uma instancia do bot usando `ENABLE_POLLING=true`; mais de uma instancia pode gerar conflito `409 Conflict` no Telegram.
- Se o Railway nao encontrar `resumo_novo_testamento.md`, o bot usa `BIBLE_SCHEDULE_URL` como fallback.
- Push para GitHub deve ser feito manualmente pelo usuario.

## Deploy Railway

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
