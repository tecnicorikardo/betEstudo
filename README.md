# Bot Telegram do cronograma de estudos

Bot Telegram para enviar a materia do cronograma todos os dias uteis as 09:40.

O deploy recomendado agora e Cloudflare Workers. A versao antiga em Python continua no repositorio como fallback para Railway ou outro worker com processo 24/7.

## Como funciona

- O bot le `cronograma_ti_20_semanas_detalhado.md`.
- O bot tambem le `Guia Completo_ Frases do Cotidiano Americano.md`.
- O bot tambem le `gramatica.md` para aulas curtas de gramatica inglesa.
- Quando configurado, o bot le um arquivo com resumos biblicos do Novo Testamento.
- A data `SCHEDULE_START_DATE` define quando comeca a Semana 1, Segunda-feira.
- De segunda a sexta, as 09:40 no fuso `America/Sao_Paulo`, ele envia a aula correspondente ao dia.
- Todos os dias, as 14:00, ele envia um resumo biblico por capitulo.
- De segunda a sexta, as 19:00, ele envia o conteudo de ingles do dia.
- O conteudo de gramatica fica disponivel pelo comando `/gramatica`; o envio automatico pode ser ligado com `GRAMMAR_ENABLED=true`.
- Se `DEEP_API_KEY` estiver configurada, a DeepSeek responde a IA e organiza o resumo biblico. Se nao houver DeepSeek, o bot usa Groq quando `GROQ_API_KEY` existir.
- O envio usa `TELEGRAM_CHAT_IDS`. Tambem da para mandar `/start` para o bot e cadastrar o chat enquanto o worker estiver rodando.

## Deploy Cloudflare Workers

Veja o passo a passo em `CLOUDFLARE_WORKERS.md`.

Resumo:

```bash
npm install
npm test
npx wrangler login
npx wrangler deploy
```

Depois do deploy, configure o webhook do Telegram apontando para a URL do Worker.

## Variaveis no Railway

Configure estas variaveis em `Environment` no Railway:

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
GROQ_API_KEY=sua_api_key_da_groq
GROQ_MODEL=llama-3.1-8b-instant
DEEP_API_KEY=sua_api_key_da_deepseek
DEEP_MODEL=deepseek-v4-flash
DEEP_BASE_URL=https://api.deepseek.com
DEEP_THINKING=disabled
ENABLE_POLLING=false
SEND_TEST_ON_START=false
```

O arquivo `token telegram.txt` fica apenas para uso local e esta no `.gitignore`.

## Comandos do bot

- `/start`: cadastra o chat atual para receber as mensagens.
- `/id`: mostra o `chat_id` do Telegram.
- `/hoje`: envia a aula calculada para hoje.
- `/amanha`: envia a aula calculada para amanha.
- `/ingles`: envia o conteudo de ingles de hoje.
- `/gramatica`: envia a aula de gramatica inglesa de hoje.
- `/biblia`: envia o resumo biblico de hoje, usando DeepSeek ou Groq quando configurada.
- `/ia sua pergunta`: responde usando DeepSeek ou Groq.
- `/ia_status`: mostra qual IA foi configurada no ambiente.
- `/cronograma`: mostra a quantidade de aulas carregadas e a data inicial.

Para usar esses comandos no Railway, configure `ENABLE_POLLING=true`. Para apenas envio diario sem respostas no chat, deixe `ENABLE_POLLING=false` e use `TELEGRAM_CHAT_IDS`.

Para testar o envio sem esperar o horario agendado, configure `SEND_TEST_ON_START=true`, faca redeploy e depois volte para `false`.

O arquivo biblico deve estar em Markdown, com um capitulo por titulo. Exemplos aceitos: `## Mateus 1`, `## Mateus - Capitulo 1`, `## Resumo de Mateus capitulo 1`.

## Teste local

Crie um `.env` baseado em `.env.example` e rode:

```bash
pip install -r requirements.txt
python bot.py --dry-run 2026-06-01
python bot.py --english-dry-run 2026-06-01
python bot.py --grammar-dry-run 2026-06-01
python bot.py --bible-dry-run 2026-06-01
python bot.py
```

No Railway, configure o servico como worker/background job usando:

```bash
python bot.py
```
