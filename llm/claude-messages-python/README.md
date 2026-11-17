# Claude with the Anthropic SDK, with prompt caching

Calls `claude-haiku-5.5` through Lovely Router with the official `anthropic` Python SDK. The only change from
stock Anthropic code is `base_url="https://lovelyrouter.com"` and the key.

It sends a long system prompt (Lovely Router's own `llms.txt`) marked with `cache_control` twice. The first call
writes the prompt cache, the second reads it, and the script prints the cache read and write tokens of each call.

## Run

```bash
export LOVELY_API_KEY=lr-...
pip install -r requirements.txt
python main.py
```

## Expected output

```text
Q: In one sentence: what does this document say a Lovely Router key starts with?
A: It says a Lovely Router API key starts with `lr-`.
   input=29 cache_write=21766 cache_read=0 output=22
   request id: req_...

Q: In one sentence: which URL does this document give for the MCP server?
A: The document gives `https://lovelyrouter.com/mcp` as the MCP server URL ...
   input=26 cache_write=0 cache_read=21766 output=56
   request id: req_...

cost: the Messages response has no cost field. ...
```

Token counts change as `llms.txt` changes.

## Cost

The Messages API response carries token usage but no cost field, so the script prints the
`x-lovely-request-id` of each call instead. The charge for each id is in Logs in the dashboard
([Usage & logs](https://lovelyrouter.com/docs/account/usage)); per-token prices are in `GET /v1/models` and on
https://lovelyrouter.com/pricing. Our test run was well under one cent.

Docs: https://lovelyrouter.com/docs/models/anthropic · https://lovelyrouter.com/docs/models/caching
