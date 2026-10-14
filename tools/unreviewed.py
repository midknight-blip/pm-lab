"""Print positive pairs from the last 4 days that nobody has checked yet,
with both sites' rules side by side. Usage: python tools/unreviewed.py [max]"""
import csv, glob, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from common import ROOT

limit = int(sys.argv[1]) if len(sys.argv) > 1 else 8
review = json.load(open(f"{ROOT}/arb/pairs_review.json")) if os.path.exists(f"{ROOT}/arb/pairs_review.json") else {}
pairs = {p["pair_id"]: p for p in json.load(open(f"{ROOT}/arb/pairs_auto.json"))["pairs"]}
best = {}
for path in sorted(glob.glob(f"{ROOT}/arb/log/*.csv"))[-4:]:
    for r in csv.DictReader(open(path)):
        e = float(r["net_edge"])
        if e > 0 and r["pair_id"] not in review:
            best[r["pair_id"]] = max(e, best.get(r["pair_id"], 0))
ranked = sorted(best.items(), key=lambda kv: -kv[1])[:limit]
if not ranked:
    print("No unchecked positive pairs.")
for pid, e in ranked:
    p = pairs.get(pid)
    print("=" * 80)
    print(f"{pid}   best net edge {e*100:.1f}c")
    if not p:
        print("(pair no longer in the matched list)")
        continue
    print(f"KALSHI  [{p['kalshi_close']}] {p['kalshi_text']}\n  {p['kalshi_rules']}")
    print(f"POLY    [{p['poly_close']}] {p['poly_text']}\n  {p['poly_rules']}")
print(f"\n{len(best)} unchecked positive pairs in total.")
