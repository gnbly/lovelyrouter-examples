# Google Maps leads to CSV

Finds local businesses on Google Maps with the emails found on their websites (`google-maps-leads`), verifies
each distinct email (`email-verify`) and writes `leads.csv`, one row per business and email. A small version of
the guide [Export Google Maps leads to CSV](https://lovelyrouter.com/guides/google-maps-leads-to-csv).

## Run

```bash
export LOVELY_API_KEY=lr-...
pip install -r requirements.txt
python main.py                                   # 5 dentists in Austin
python main.py "coffee shop" "Denver, CO, USA" 10
```

## Expected output

```text
google-maps-leads: succeeded, 5 results, charged $0.00255  (run_...)
email-verify: succeeded, 4 results, charged $0.006  (run_...)
  River Rock Dental Austin - Mueller  +1 512-...  (no email found)
  Shoal Creek Dental Care  +1 512-...  hello@...
  ...

wrote leads.csv: 5 places, 4 emails checked
cost: $0.008550 (sum of charge_usd from the runs above)
```

## Cost

Each run returns `charge_usd`, and the script adds them up. Both tools bill per result, and `max_results` caps
each run: the run holds the most it can cost and settles to what it returned. Live prices:
[Google Maps leads](https://lovelyrouter.com/tools) and https://lovelyrouter.com/pricing.

Use the data responsibly: check local rules on cold outreach before you email anyone on the list.

Docs: https://lovelyrouter.com/docs/tools/run
