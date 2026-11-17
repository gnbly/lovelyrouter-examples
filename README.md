# Lovely Router examples

Small, runnable examples for [Lovely Router](https://lovelyrouter.com): a hosted MCP server, pay-per-result web
data tools and a browser agent, plus Claude, GPT and Gemini on the same prepaid key at official list prices.

Each folder has a README, runs with one command and prints what the run cost (or, where the API response has no
cost field, the request id to look the charge up). Create a key at https://lovelyrouter.com/signup (top up from
$5, no subscription; see https://lovelyrouter.com/pricing), then:

```bash
export LOVELY_API_KEY=lr-...
cd mcp/python-mcp-client && pip install -r requirements.txt && python main.py
```

## MCP server

`https://lovelyrouter.com/mcp` (streamable HTTP, `Authorization: Bearer $LOVELY_API_KEY`) exposes web search,
page reading (`web_fetch`), the data tool catalog (`suggest_tools`, `get_tool`, `run_tool` ...), the browser
agent and image generation.

| Example | What it shows | Cost of our test run |
| --- | --- | --- |
| [mcp/claude-code.md](mcp/claude-code.md) | Add the server to Claude Code with one command or a `.mcp.json` | setup only |
| [mcp/cursor.md](mcp/cursor.md) | Add the server to Cursor (`~/.cursor/mcp.json`) | setup only |
| [mcp/python-mcp-client](mcp/python-mcp-client) | List the tools and call `web_search` with the `mcp` Python SDK | $0.0009 |

The [`.mcp.json`](.mcp.json) at the root of this repo is the Cursor config for the server.

## Data tools and browser agent (REST)

| Example | What it shows | Cost of our test run |
| --- | --- | --- |
| [data-tools/google-maps-leads-csv](data-tools/google-maps-leads-csv) | Google Maps businesses with emails, verified, saved as CSV | $0.00855 |
| [browser-agent/form-fill-python](browser-agent/form-fill-python) | A browser agent run fills and submits a public test form, returns JSON | $0.03 |

## LLM APIs

The same key works with the official Anthropic, OpenAI and Google SDKs; change the base URL and the key.

| Example | What it shows | Cost |
| --- | --- | --- |
| [llm/claude-messages-python](llm/claude-messages-python) | Anthropic SDK with prompt caching, prints cache read/write tokens | no cost field; request ids printed |
| [llm/openai-node](llm/openai-node) | OpenAI Node SDK, streaming with usage | no cost field; request id printed |

Docs: https://lovelyrouter.com/docs · Machine-readable: https://lovelyrouter.com/llms.txt ·
Prices: https://lovelyrouter.com/pricing

## Contributing

Contributions that add an example are welcome. Keep it under 100 lines, read the key from `LOVELY_API_KEY`,
print what the run cost, and include the output of a real run in its README.

## License

[MIT](LICENSE)
