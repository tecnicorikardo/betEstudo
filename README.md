# Bot Telegram do cronograma de estudos

Worker em Python para enviar a materia do cronograma todos os dias uteis as 09:40.

## Como funciona

- O bot le `cronograma_ti_20_semanas_detalhado.md`.
- A data `SCHEDULE_START_DATE` define quando comeca a Semana 1, Segunda-feira.
- De segunda a sexta, as 09:40 no fuso `America/Sao_Paulo`, ele envia a aula correspondente ao dia.
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
```

O arquivo `token telegram.txt` fica apenas para uso local e esta no `.gitignore`.

## Comandos do bot

- `/start`: cadastra o chat atual para receber as mensagens.
- `/id`: mostra o `chat_id` do Telegram.
- `/hoje`: envia a aula calculada para hoje.
- `/amanha`: envia a aula calculada para amanha.
- `/cronograma`: mostra a quantidade de aulas carregadas e a data inicial.

## Teste local

Crie um `.env` baseado em `.env.example` e rode:

```bash
pip install -r requirements.txt
python bot.py --dry-run 2026-06-01
python bot.py
```

No Railway, o `Procfile` inicia o worker com:

```bash
python bot.py
```
