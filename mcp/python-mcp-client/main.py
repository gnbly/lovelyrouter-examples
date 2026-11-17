"""List the Lovely Router MCP tools, then call web_search once."""
import asyncio
import os
import re

import httpx2
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

URL = "https://lovelyrouter.com/mcp"
HEADERS = {"Authorization": f"Bearer {os.environ['LOVELY_API_KEY']}"}


async def main():
    async with httpx2.AsyncClient(headers=HEADERS, timeout=120) as http, \
            streamable_http_client(URL, http_client=http) as (read, write), \
            ClientSession(read, write) as session:
        await session.initialize()

        tools = (await session.list_tools()).tools
        print(f"{len(tools)} tools: " + ", ".join(t.name for t in tools))

        result = await session.call_tool(
            "web_search", {"query": "Model Context Protocol specification", "count": 3}
        )
        text = "\n".join(c.text for c in result.content if c.type == "text")

        # Print the header line and each result's title + URL, not the full summaries.
        lines = text.splitlines()
        print("\n" + lines[0])
        for i, line in enumerate(lines):
            if re.match(r"^\d+\. ", line):
                print(line.strip())
                print("   " + lines[i + 1].strip())

        # The answer's first line carries the charge, e.g. "· charged $0.0009".
        charge = re.search(r"charged \$[\d.]+", lines[0])
        print("\ncost:", charge.group(0) if charge else "no charge in the answer; see Tools in the dashboard")


asyncio.run(main())
