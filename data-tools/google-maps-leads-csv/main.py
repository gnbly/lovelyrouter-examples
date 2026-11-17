"""Google Maps leads to CSV: find businesses, verify their emails, write leads.csv.

A small version of https://lovelyrouter.com/guides/google-maps-leads-to-csv
Usage: python main.py ["search term"] ["location"] [max places]
"""
import csv
import os
import sys

import requests

BASE = "https://lovelyrouter.com/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['LOVELY_API_KEY']}"}

TERM = sys.argv[1] if len(sys.argv) > 1 else "dentist"
AREA = sys.argv[2] if len(sys.argv) > 2 else "Austin, Texas, USA"
MAX_PLACES = int(sys.argv[3]) if len(sys.argv) > 3 else 5
total_charge = 0.0


def run_tool(tool, tool_input, max_results):
    """Start a run, poll while it answers 202, return the items (see /docs/tools/run)."""
    global total_charge
    res = requests.post(f"{BASE}/tools/{tool}/run", headers=HEADERS,
                        json={"input": tool_input, "max_results": max_results}, timeout=90)
    run = res.json()
    if not res.ok:
        raise RuntimeError(run["error"]["message"])
    while res.status_code == 202:
        res = requests.get(f"{BASE}/tools/runs/{run['id']}", headers=HEADERS,
                           params={"wait": 60}, timeout=90)
        res.raise_for_status()
        run = res.json()
    print(f"{tool}: {run['status']}, {run['results']} results, charged ${run['charge_usd']}  ({run['id']})")
    total_charge += run["charge_usd"] or 0
    return run["items"] or []


# 1. Places with the emails found on their websites.
places = run_tool(
    "google-maps-leads",
    {"searchTerms": [TERM], "location": AREA, "websiteFilter": "withWebsite"},
    max_results=MAX_PLACES,
)

# 2. Verify each distinct address once.
emails = sorted({e.strip().lower() for p in places for e in p.get("emails") or []})
checks = {}
if emails:
    for check in run_tool("email-verify", {"emails": emails}, max_results=len(emails)):
        # Each check includes the address it tested: index it by that address.
        addr = next((v.lower() for v in check.values() if isinstance(v, str) and v.lower() in emails), None)
        if addr:
            checks[addr] = check
check_fields = sorted({k for c in checks.values() for k, v in c.items() if not isinstance(v, (dict, list))})

# 3. One row per business and email address.
fields = ["name", "address", "phone", "website", "email", "rating", "reviews", "maps_url"]
fields += [f"check_{k}" for k in check_fields]
with open("leads.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for p in places:
        row = {
            "name": p.get("title"),
            "address": p.get("formattedAddress"),
            "phone": p.get("phoneIntl") or p.get("phone"),
            "website": p.get("website"),
            "rating": p.get("rating"),
            "reviews": p.get("reviewCount"),
            "maps_url": p.get("googleMapsUri"),
        }
        for email in sorted({e.strip().lower() for e in p.get("emails") or []}) or [""]:
            check = checks.get(email, {})
            writer.writerow({**row, "email": email, **{f"check_{k}": check.get(k) for k in check_fields}})
        print(f"  {row['name']}  {row['phone'] or ''}  {', '.join(p.get('emails') or []) or '(no email found)'}")

print(f"\nwrote leads.csv: {len(places)} places, {len(emails)} emails checked")
print(f"cost: ${total_charge:.6f} (sum of charge_usd from the runs above)")
