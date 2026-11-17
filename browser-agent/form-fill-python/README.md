# Browser agent: fill and submit a form

Starts a browser agent run on httpbin's public test form (`https://httpbin.org/forms/post`), which echoes what
it receives. The agent fills three fields, submits the form and returns the echoed values as JSON in `data`,
built from an `output_schema`.

The run is capped with `max_steps: 10` and set to never pause for a person (`"human": false`,
`"approve": "none"`), so it holds at most 10 steps at the fast-mode price while it runs and then settles to the
steps it took.

## Run

```bash
export LOVELY_API_KEY=lr-...
pip install -r requirements.txt
python main.py
```

## Expected output

```text
started brun_... running
  status: succeeded steps: 5

status: succeeded | steps: 5
answer: The order was submitted successfully. The response page shows custname = "Ada Lovelace" and size = "medium".
data: {"custname": "Ada Lovelace", "size": "medium"}
cost: $0.03 (charge_usd from the run object)
```

## Cost

Read from `charge_usd` on the finished run: steps taken times the step price of the mode. Live step prices:
https://lovelyrouter.com/browser-agent and [Modes, models & pricing](https://lovelyrouter.com/docs/browser-agent/modes).

Docs: https://lovelyrouter.com/docs/browser-agent
