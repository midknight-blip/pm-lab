"""Every 15 minutes: price every matched pair and log the arbitrage math.

For each pair, two ways to lock in $1:
  A) buy YES on Kalshi + buy NO on Polymarket
  B) buy YES on Polymarket + buy NO on Kalshi
net_edge = 1 - cost - fees, per $1 contract, at the best price only.

Writes arb/log/DATE.csv and arb/health.json
"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import *  # noqa

LEG_CAP = 50  # contracts per leg we'd realistically trade with a small account
FIELDS = ["ts", "pair_id", "dir", "k_price", "p_price", "cost", "fees", "net_edge",
          "size", "profit_avail", "days", "annualized", "score", "review"]


def load_pairs():
    pairs = json.load(open(f"{ROOT}/arb/pairs_auto.json"))["pairs"]
    review = {}
    rp = f"{ROOT}/arb/pairs_review.json"
    if os.path.exists(rp):
        review = json.load(open(rp))
    out = []
    for p in pairs:
        r = review.get(p["pair_id"], {}).get("status", "unreviewed")
        if r == "different":
            continue
        p["review"] = r
        out.append(p)
    return out


def edges(pair, kq, pq, ts):
    rows = []
    close = max(parse_ts(pair["kalshi_close"]), parse_ts(pair["poly_close"]))
    days = max((close - ts).total_seconds() / 86400, 0.5)
    legs = [
        ("K_yes+P_no", kq["yes_ask"], kq["yes_ask_size"], pq["no_ask"], pq["no_ask_size"]),
        ("P_yes+K_no", kq["no_ask"], kq["no_ask_size"], pq["yes_ask"], pq["yes_ask_size"]),
    ]
    for d, kp, ks, pp, ps in legs:
        if kp is None or pp is None or kp <= 0 or pp <= 0 or kp >= 1 or pp >= 1:
            continue
        size = min(ks or 0, ps or 0, LEG_CAP)
        n = max(size, 1)
        fees = (kalshi_fee(kp, n) + poly_fee(pp, n, pair["poly_fee_rate"])) / n
        cost = kp + pp
        net = 1 - cost - fees
        ann = net / (cost + fees) * 365 / days if cost + fees > 0 else 0
        rows.append({"ts": iso(ts), "pair_id": pair["pair_id"], "dir": d,
                     "k_price": kp, "p_price": pp, "cost": round(cost, 4),
                     "fees": round(fees, 4), "net_edge": round(net, 4), "size": round(size, 2),
                     "profit_avail": round(max(net, 0) * size, 2), "days": round(days, 2),
                     "annualized": round(ann, 4), "score": pair["score"], "review": pair["review"]})
    return rows


def snapshot(pairs):
    ts = now()
    km = kalshi_markets_by_ticker({p["kalshi_ticker"] for p in pairs})
    books = poly_books({p["poly_token"] for p in pairs})
    rows, ok = [], 0
    for p in pairs:
        m, b = km.get(p["kalshi_ticker"]), books.get(p["poly_token"])
        if not m or not b:
            continue
        ok += 1
        rows += edges(p, kalshi_quote(m), poly_quote(b), ts)
    return ts, rows, ok


def append(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerows(rows)


def main():
    pairs = load_pairs()
    err = None
    try:
        ts, rows, ok = snapshot(pairs)
        # keep the repo small: only log pairs within 5 cents of an arb
        append(f"{ROOT}/arb/log/{ts:%Y-%m-%d}.csv", [r for r in rows if r["net_edge"] > -0.05])
    except Exception as e:  # record the failure so the summary shows it
        ts, rows, ok, err = now(), [], 0, repr(e)[:300]
    best = max((r["net_edge"] for r in rows), default=None)
    pos = sum(r["net_edge"] > 0 for r in rows)
    runs = f"{ROOT}/arb/runs.csv"
    new = not os.path.exists(runs)
    with open(runs, "a") as fh:
        if new:
            fh.write("ts,pairs_watched,pairs_priced,best_edge,n_positive,error\n")
        fh.write(f"{iso(ts)},{len(pairs)},{ok},{best if best is not None else ''},{pos},{'1' if err else ''}\n")
    health = {"last_scan": iso(ts), "pairs_watched": len(pairs), "pairs_priced": ok,
              "rows": len(rows), "positive_now": pos, "best_edge_now": best, "error": err}
    with open(f"{ROOT}/arb/health.json", "w") as fh:
        json.dump(health, fh, indent=1)
    print(json.dumps(health))


if __name__ == "__main__":
    main()
