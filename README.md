# Bot Telegram do cronograma de estudos

Worker em Python para enviar a materia do cronograma todos os dias uteis as 09:40.

## Como funciona

- O bot le `cronograma_ti_20_semanas_detalhado.md`.
- O bot tambem le `Guia Completo_ Frases do Cotidiano Americano.md`.
- A data `SCHEDULE_START_DATE` define quando comeca a Semana 1, Segunda-feira.
- De segunda a sexta, as 09:40 no fuso `America/Sao_Paulo`, ele envia a aula correspondente ao dia.
- De segunda a sexta, as 19:00, ele envia o conteudo de ingles do dia.
- O envio usa `TELEGRAM_CHAT_IDS`. Tambem da para mandar `/start` para o bot e cadastrar o chat enquanto o worker estiver rodando.

## Variaveis no Railway

Configure estas variaveis em `Variables` no Railway:

```env
TELEGRAM_BOT_TOKEN=seu_token_do_bot
TELEGRAM_CHAT_IDS=seu_chat_id
SCHEDULE_START_DATE=2026-06-01
TIMEZONE=America/Sao_Paulo
SEND_HOUR=9
SEND_MINUTE=40
ENGLISH_SCHEDULE_FILE=Guia Completo_ Frases do Cotidiano Americano.md
ENGLISH_SEND_HOUR=19
ENGLISH_SEND_MINUTE=0
ENABLE_POLLING=false
SEND_TEST_ON_START=false
```

O arquivo `token telegram.txt` fica apenas para uso local e esta no `.gitignore`.

## Comandos do bot

- `/start`: cadastra o chat atual para receber as mensagens.
- `/id`: mostra o `chat_id` do Telegram.
- `/hoje`: envia a aula calculada para hoje.
- `/amanha`: envia a aula calculada para amanha.
- `/cronograma`: mostra a quantidade de aulas carregadas e a data inicial.

Para usar esses comandos no Railway, configure `ENABLE_POLLING=true` temporariamente. Para o envio diario, deixe `ENABLE_POLLING=false` e use `TELEGRAM_CHAT_IDS`.

Para testar o envio sem esperar o horario agendado, configure `SEND_TEST_ON_START=true`, faca redeploy e depois volte para `false`.

## Teste local

Crie um `.env` baseado em `.env.example` e rode:

```bash
pip install -r requirements.txt
python bot.py --dry-run 2026-06-01
python bot.py --english-dry-run 2026-06-01
python bot.py
```

No Railway, o `Procfile` inicia o worker com:

```bash
python bot.py
```
