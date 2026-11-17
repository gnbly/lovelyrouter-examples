# Python MCP client

Connects to the Lovely Router MCP server (`https://lovelyrouter.com/mcp`, streamable HTTP) with the official
`mcp` Python SDK, lists the tools it exposes, and calls `web_search` once.

## Run

```bash
export LOVELY_API_KEY=lr-...
pip install -r requirements.txt
python main.py
```

## Expected output

```text
13 tools: web_search, web_fetch, generate_image, get_image, search_tools, suggest_tools, get_tool, run_tool, get_run, browser_run, browser_status, browser_reply, browser_takeover

Web search: 3 result(s) for "Model Context Protocol specification" · charged $0.0009
1. ...
   https://modelcontextprotocol.io/specification/...
2. ...
3. ...

cost: charged $0.0009
```

The cost is read from the first line of the `web_search` answer. One search costs one call at the
[live price](https://lovelyrouter.com/pricing); a search with no results costs nothing.

Docs: https://lovelyrouter.com/docs/tools/mcp
