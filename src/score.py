"""Daily: check which forecast markets have settled and score Claude vs the market.

Brier score = (probability - outcome)^2, lower is better.
Paper bet: when Claude's number beats the price by 5+ points, buy 1 contract
at the ask (after fees) and track the result.
Writes forecast/forecasts.csv (outcomes) and forecast/scores.json
"""
import json, math, os, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from common import *  # noqa
from forecast_common import read_fc, write_fc

EDGE = 0.05


def resolve(key):
    site, mid = key.split(":", 1)
    if site == "kalshi":
        m = kalshi_market(mid)
        if m.get("status") in ("finalized", "settled", "determined") and m.get("result") in ("yes", "no"):
            return 1.0 if m["result"] == "yes" else 0.0
        return None
    m = http(f"{GAMMA}/markets/{mid}")
    if not m.get("closed"):
        return None
    try:
        p = [float(x) for x in json.loads(m.get("outcomePrices") or "[]")]
    except Exception:
        return None
    if p and p[0] >= 0.99:
        return 1.0
    if p and p[0] <= 0.01:
        return 0.0
    return "void" if p else None


def fee(key, price, rate):
    if key.startswith("kalshi:"):
        return kalshi_fee(price, 10) / 10
    return poly_fee(price, 1, rate)


def paper_bet(r):
    me, bid, ask, o = float(r["my_prob"]), float(r["mkt_bid"]), float(r["mkt_ask"]), float(r["outcome"])
    rate = float(r.get("fee_rate") or 0)
    if me - ask >= EDGE:
        return "yes", o - ask - fee(r["key"], ask, rate), ask
    if bid - me >= EDGE:
        no_price = 1 - bid
        return "no", (1 - o) - no_price - fee(r["key"], no_price, rate), no_price
    return None, 0.0, 0.0


def stats(rows):
    diffs = [(float(r["my_prob"]) - float(r["outcome"])) ** 2 - (float(r["mkt_mid"]) - float(r["outcome"])) ** 2 for r in rows]
    n = len(diffs)
    if not n:
        return {"n": 0}
    me = sum((float(r["my_prob"]) - float(r["outcome"])) ** 2 for r in rows) / n
    mk = sum((float(r["mkt_mid"]) - float(r["outcome"])) ** 2 for r in rows) / n
    mean = sum(diffs) / n
    sd = math.sqrt(sum((d - mean) ** 2 for d in diffs) / (n - 1)) if n > 1 else 0
    bets = [paper_bet(r) for r in rows]
    placed = [b for b in bets if b[0]]
    staked = sum(b[2] for b in placed)
    pnl = sum(b[1] for b in placed)
    return {"n": n, "brier_claude": round(me, 4), "brier_market": round(mk, 4),
            "claude_minus_market": round(mean, 4), "std_error": round(sd / math.sqrt(n), 4) if n > 1 else None,
            "paper_bets": len(placed), "paper_staked": round(staked, 2), "paper_pnl": round(pnl, 3),
            "paper_roi": round(pnl / staked, 3) if staked else None,
            "bet_wins": sum(1 for b in placed if b[1] > 0)}


def main():
    rows = read_fc()
    for r in rows:
        if r.get("outcome") or not r.get("mkt_mid"):
            continue
        close = parse_ts(r.get("close"))
        if close and close > now():
            continue
        try:
            o = resolve(r["key"])
        except Exception as e:
            print("resolve failed", r["key"], e)
            continue
        if o is not None:
            r["outcome"] = o if o == "void" else int(o)
            r["resolved_at"] = iso()
    write_fc(rows)
    done = [r for r in rows if r.get("outcome") not in ("", None, "void") and r.get("mkt_mid")]
    by_cat = defaultdict(list)
    for r in done:
        by_cat[r["category"]].append(r)
    big = [r for r in done if abs(float(r["my_prob"]) - float(r["mkt_mid"])) >= 0.10]
    out = {"updated": iso(), "forecasts_made": len(rows),
           "awaiting_price": sum(1 for r in rows if not r.get("mkt_mid")),
           "pending": sum(1 for r in rows if not r.get("outcome")),
           "void": sum(1 for r in rows if r.get("outcome") == "void"),
           "all": stats(done), "disagree_10pts_plus": stats(big),
           "by_category": {c: stats(v) for c, v in sorted(by_cat.items())}}
    with open(f"{ROOT}/forecast/scores.json", "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out["all"]))


if __name__ == "__main__":
    main()
