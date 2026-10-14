"""Mon/Thu before the check-in: choose a batch of markets for Claude to forecast.

The queue file deliberately leaves out prices so the forecast is made blind.
Writes forecast/queue/DATE.json
"""
import glob, json, os, random, sys
from collections import defaultdict
from datetime import timedelta
sys.path.insert(0, os.path.dirname(__file__))
from common import *  # noqa
from forecast_common import read_fc

N = int(os.environ.get("FORECAST_N", "10"))
CAPS = {"sports": 2, "crypto": 1}  # little chance of an edge there; keep a few as a control


def seen_keys():
    keys = {r["key"] for r in read_fc()}
    for p in glob.glob(f"{ROOT}/forecast/queue/*.json"):
        keys |= {q["key"] for q in json.load(open(p))["markets"]}
    return keys


def poly_category(m):
    ft = (m.get("feeType") or "").lower()
    q = m.get("question", "").lower()
    if ft.startswith("sports") or " vs" in q or "spread:" in q or "o/u" in q:
        return "sports"
    for k in ("crypto", "economics", "politics", "finance", "tech", "weather", "culture", "geopolitics"):
        if k in ft:
            return k
    if any(w in q for w in ("bitcoin", "ethereum", "solana", "btc", "eth ")):
        return "crypto"
    return "other"


def kalshi_category(e):
    c = (e.get("category") or "other").lower()
    if "sport" in c:
        return "sports"
    if "crypto" in c:
        return "crypto"
    return c


def candidates():
    lo, hi = now() + timedelta(days=2), now() + timedelta(days=30)
    out = []
    for e in kalshi_open_events():
        for m in e.get("markets", []):
            q = kalshi_quote(m)
            close = parse_ts(m.get("expected_expiration_time")) or parse_ts(m.get("close_time"))
            if not close or not (lo <= close <= hi) or q["yes_bid"] is None or q["yes_ask"] is None:
                continue
            mid = (q["yes_bid"] + q["yes_ask"]) / 2
            if q["yes_ask"] - q["yes_bid"] > 0.10 or not (0.07 <= mid <= 0.93):
                continue
            if f(m.get("volume_24h_fp"), 0) < 200:
                continue
            out.append({"key": f"kalshi:{m['ticker']}", "group": e["event_ticker"],
                        "question": f"{e.get('title','')} — {m.get('yes_sub_title') or ''}".strip(" —"),
                        "rules": ((m.get("rules_primary") or "") + " " + (m.get("rules_secondary") or ""))[:1200],
                        "close": iso(close), "category": kalshi_category(e),
                        "link": f"https://kalshi.com/markets/{e.get('series_ticker','').lower()}",
                        "vol": f(m.get("volume_24h_fp"), 0)})
    for m in poly_open_markets():
        if not poly_is_binary_yes_no(m):
            continue
        close = parse_ts(m.get("endDate"))
        bb, ba = f(m.get("bestBid")), f(m.get("bestAsk"))
        if not close or not (lo <= close <= hi) or bb is None or ba is None:
            continue
        mid = (bb + ba) / 2
        if ba - bb > 0.06 or not (0.07 <= mid <= 0.93) or f(m.get("volume24hr"), 0) < 2000:
            continue
        out.append({"key": f"poly:{m['id']}", "group": m.get("negRiskMarketID") or f"p{m['id']}",
                    "question": m.get("question", ""), "rules": (m.get("description") or "")[:1200],
                    "close": iso(close), "category": poly_category(m),
                    "link": f"https://polymarket.com/market/{m.get('slug','')}",
                    "vol": f(m.get("volume24hr"), 0)})
    return out


def choose(cands, n):
    seen = seen_keys()
    by_cat = defaultdict(list)
    for c in cands:
        if c["key"] not in seen:
            by_cat[c["category"]].append(c)
    rng = random.Random(now().strftime("%Y%m%d"))
    for cat in by_cat:  # favour liquid markets but keep some variety
        by_cat[cat].sort(key=lambda c: c["vol"], reverse=True)
        top = by_cat[cat][:40]
        rng.shuffle(top)
        by_cat[cat] = top
    picked, groups, count = [], set(), defaultdict(int)
    cats = sorted(by_cat, key=lambda c: -len(by_cat[c]))
    while len(picked) < n and any(by_cat.values()):
        progressed = False
        for cat in cats:
            if len(picked) >= n:
                break
            if count[cat] >= CAPS.get(cat, n):
                continue
            while by_cat[cat]:
                c = by_cat[cat].pop(0)
                if c["group"] in groups:
                    continue
                picked.append(c); groups.add(c["group"]); count[cat] += 1; progressed = True
                break
        if not progressed:
            break
    return picked


def main():
    picked = choose(candidates(), N)
    os.makedirs(f"{ROOT}/forecast/queue", exist_ok=True)
    batch = now().strftime("%Y-%m-%d")
    for p in picked:
        p.pop("vol", None); p.pop("group", None); p.pop("link", None)  # links show the price
    with open(f"{ROOT}/forecast/queue/{batch}.json", "w") as fh:
        json.dump({"batch": batch, "created": iso(), "markets": picked}, fh, indent=1)
    print(f"queued {len(picked)} markets for {batch}")


if __name__ == "__main__":
    main()
