"""Fill and submit a public demo form with the Lovely Router browser agent.

The target is httpbin's test form, which echoes what it receives. Each field
the agent fills takes about one step. The run is capped at 10 steps and never
pauses for a person, so the most it can hold is 10 x the fast-mode step price
(see https://lovelyrouter.com/docs/browser-agent/modes).
"""
import json
import os

import requests

API = "https://lovelyrouter.com/v1/browser"
H = {"Authorization": f"Bearer {os.environ['LOVELY_API_KEY']}"}

run = requests.post(f"{API}/runs", headers=H, timeout=60, json={
    "goal": (
        "On the pizza order form, set customer name 'Ada Lovelace', email 'ada@example.com' "
        "and size Medium; leave every other field as it is. Submit the order, then report the "
        "custname and size values shown on the response page."
    ),
    "start_url": "https://httpbin.org/forms/post",
    "mode": "fast",
    "max_steps": 10,
    "human": False,      # never ask questions or hand over
    "approve": "none",   # submit without waiting for approval
    "output_schema": {
        "type": "object",
        "properties": {"custname": {"type": "string"}, "size": {"type": "string"}},
        "required": ["custname", "size"],
    },
}).json()
if "id" not in run:
    raise SystemExit(f"could not start the run: {run}")
print("started", run["id"], run["status"])

# Each GET holds up to 30 s and returns as soon as the status changes.
while run["status"] == "running":
    run = requests.get(f"{API}/runs/{run['id']}", headers=H, params={"wait": 30}, timeout=60).json()
    print("  status:", run["status"], "steps:", run.get("steps"))

# The charge settles a few seconds after the run ends.
for _ in range(10):
    if run.get("charge_usd") is not None:
        break
    run = requests.get(f"{API}/runs/{run['id']}", headers=H, params={"wait": 5}, timeout=60).json()

print("\nstatus:", run["status"], "| steps:", run.get("steps"))
print("answer:", run.get("answer"))
print("data:", json.dumps(run.get("data")))
if run.get("error"):
    print("error:", run["error"])
print(f"cost: ${run.get('charge_usd')} (charge_usd from the run object)")
