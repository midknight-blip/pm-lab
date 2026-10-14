"""Append a batch of forecasts. Usage: python tools/add_forecasts.py batch.json

batch.json: {"batch": "YYYY-MM-DD", "forecasts": [
  {"key": "kalshi:TICKER", "my_prob": 0.62, "saw_market_price": false, "reason": "one line"}, ...]}
Question, close date and category are copied from the queue file."""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from common import ROOT, iso
from forecast_common import read_fc, write_fc

data = json.load(open(sys.argv[1]))
queue = {q["key"]: q for q in json.load(open(f"{ROOT}/forecast/queue/{data['batch']}.json"))["markets"]}
rows = read_fc()
have = {r["key"] for r in rows}
added = 0
for fc in data["forecasts"]:
    q = queue.get(fc["key"])
    p = float(fc["my_prob"])
    if not q or fc["key"] in have or not 0 <= p <= 1:
        print("skipped", fc["key"])
        continue
    rows.append({"key": fc["key"], "batch": data["batch"], "made_at": iso(), "question": q["question"],
                 "close": q["close"], "category": q["category"], "my_prob": round(p, 3),
                 "saw_market_price": "yes" if fc.get("saw_market_price") else "no",
                 "reason": fc.get("reason", "")[:200].replace("\n", " ")})
    added += 1
write_fc(rows)
print(f"added {added} forecasts")
