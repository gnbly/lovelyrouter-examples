"""Call Claude with the Anthropic SDK through Lovely Router and show prompt caching.

The same long system prompt (Lovely Router's own llms.txt) is sent twice with
cache_control. The first call writes the cache, the second reads it.
"""
import os

import anthropic
import requests

MODEL = "claude-haiku-5.5"

client = anthropic.Anthropic(
    base_url="https://lovelyrouter.com",  # the only change from stock Anthropic code
    api_key=os.environ["LOVELY_API_KEY"],
)

reference = requests.get("https://lovelyrouter.com/llms.txt", timeout=30).text
system = [{"type": "text", "text": reference, "cache_control": {"type": "ephemeral"}}]

questions = [
    "In one sentence: what does this document say a Lovely Router key starts with?",
    "In one sentence: which URL does this document give for the MCP server?",
]

for question in questions:
    raw = client.messages.with_raw_response.create(
        model=MODEL,
        max_tokens=100,
        system=system,
        messages=[{"role": "user", "content": question}],
    )
    msg = raw.parse()
    u = msg.usage
    print(f"Q: {question}")
    print(f"A: {msg.content[0].text.strip()}")
    print(
        f"   input={u.input_tokens} cache_write={u.cache_creation_input_tokens} "
        f"cache_read={u.cache_read_input_tokens} output={u.output_tokens}"
    )
    print(f"   request id: {raw.headers.get('x-lovely-request-id')}\n")

print(
    "cost: the Messages response has no cost field. The charge for each request id is in "
    "Logs (https://lovelyrouter.com/app/logs); per-token prices are in GET /v1/models."
)
