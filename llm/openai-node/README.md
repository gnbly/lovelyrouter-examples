# GPT with the OpenAI Node SDK

Streams a reply from `gpt-5.6-luna` through Lovely Router with the official `openai` Node SDK, then prints the
token usage and the request id. The only change from stock OpenAI code is
`baseURL: 'https://lovelyrouter.com/v1'` and the key.

## Run

Node.js 18 or newer.

```bash
export LOVELY_API_KEY=lr-...
npm install
npm start
```

## Expected output

```text
Packets find their way
Through the dark, the routers hum
Worlds connect unseen

model: gpt-5.6-luna
tokens: prompt=13 cached=0 completion=160
request id: req_...
cost: the Chat Completions response has no cost field. ...
```

The completion count includes reasoning tokens.

## Cost

The response carries token usage (`stream_options.include_usage`) but no cost field, so the script prints the
`x-lovely-request-id`. The charge for that id is in Logs in the dashboard
([Usage & logs](https://lovelyrouter.com/docs/account/usage)); per-token prices are in `GET /v1/models` and on
https://lovelyrouter.com/pricing.

Docs: https://lovelyrouter.com/docs/models/openai
