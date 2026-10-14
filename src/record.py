"""Runs right after Claude pushes forecasts: stamp each new forecast with the
market's price at that moment, so the comparison is fair."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import *  # noqa
from forecast_common import read_fc, write_fc


def quote_for(key):
    site, mid = key.split(":", 1)
    if site == "kalshi":
        q = kalshi_quote(kalshi_market(mid))
        return q["yes_bid"], q["yes_ask"], KALSHI_FEE_RATE
    m = http(f"{GAMMA}/markets/{mid}")
    return f(m.get("bestBid")), f(m.get("bestAsk")), poly_fee_rate(m)


def main():
    rows, n = read_fc(), 0
    for r in rows:
        if r.get("mkt_mid"):
            continue
        try:
            bid, ask, fee = quote_for(r["key"])
        except Exception as e:
            print("price failed", r["key"], e)
            continue
        if bid is None or ask is None:
            continue
        r.update(mkt_bid=bid, mkt_ask=ask, mkt_mid=round((bid + ask) / 2, 4), fee_rate=fee, price_ts=iso())
        n += 1
    write_fc(rows)
    print(f"stamped {n} forecasts")


if __name__ == "__main__":
    main()
