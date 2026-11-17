# Lovely Router MCP server in Claude Code

The server at `https://lovelyrouter.com/mcp` (streamable HTTP) gives Claude Code web search, page reading
(`web_fetch`), pay-per-result data tools, a cloud browser agent and image generation. It uses your Lovely Router
API key in `LOVELY_API_KEY`.

## Add it with one command

```bash
export LOVELY_API_KEY=lr-...
claude mcp add --transport http lovely-tools https://lovelyrouter.com/mcp \
  --header "Authorization: Bearer $LOVELY_API_KEY"
```

This adds it to the current project. Add `--scope user` to use it in every project, then check it with:

```bash
claude mcp list
```

## Or commit it for your team

Claude Code reads a `.mcp.json` at the project root and expands `${LOVELY_API_KEY}` from each person's
environment, so the key stays out of the file:

```json
{
  "mcpServers": {
    "lovely-tools": {
      "type": "http",
      "url": "https://lovelyrouter.com/mcp",
      "headers": { "Authorization": "Bearer ${LOVELY_API_KEY}" }
    }
  }
}
```

(The `.mcp.json` at the root of this repo uses Cursor's `${env:LOVELY_API_KEY}` syntax instead; see
[cursor.md](cursor.md).)

## What you get

`tools/list` returns 13 tools: `web_search`, `web_fetch`, `generate_image`, `get_image`, `search_tools`,
`suggest_tools`, `get_tool`, `run_tool`, `get_run`, `browser_run`, `browser_status`, `browser_reply` and
`browser_takeover`. `run_tool` reaches the whole data tool catalog; see the live list and prices at
https://lovelyrouter.com/tools.

Give the agent a key with a spend limit and ask it to set `max_results` on every run. `suggest_tools`,
`search_tools` and `get_tool` are free and show the price before anything runs.

Docs: https://lovelyrouter.com/docs/tools/mcp
