# Lovely Router MCP server in Cursor

The server at `https://lovelyrouter.com/mcp` (streamable HTTP) gives Cursor's agent web search, page reading
(`web_fetch`), pay-per-result data tools, a cloud browser agent and image generation.

## Configure it

Add the server to `~/.cursor/mcp.json` for every project, or to `.cursor/mcp.json` in one project:

```json
{
  "mcpServers": {
    "lovely-tools": {
      "url": "https://lovelyrouter.com/mcp",
      "headers": { "Authorization": "Bearer ${env:LOVELY_API_KEY}" }
    }
  }
}
```

Cursor resolves `${env:LOVELY_API_KEY}` from your environment, so set it in your shell profile
(`export LOVELY_API_KEY=lr-...`) and restart Cursor. You can also paste the key in place of the variable, as the
[Cursor guide](https://lovelyrouter.com/guides/mcp-tools-for-cursor) shows; then keep that file out of version
control.

The server then appears in Cursor's MCP settings with 13 tools, where you can check that it is connected.

## Check it from a terminal

```bash
curl https://lovelyrouter.com/mcp \
  -H "Authorization: Bearer $LOVELY_API_KEY" \
  -H "content-type: application/json" \
  -d '{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}'
```

## Cost

Tools are billed per use from your prepaid balance: web search and page reading per call, data tools per result,
the browser agent per step, images per image. Live prices: https://lovelyrouter.com/pricing. Use a key with a
spend limit for agents: a call that could take the key past its limit is refused with `402` before anything is
charged.

Guide: https://lovelyrouter.com/guides/mcp-tools-for-cursor · Docs: https://lovelyrouter.com/docs/tools/mcp
