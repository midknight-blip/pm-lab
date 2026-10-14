import csv, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import ROOT

FC_PATH = f"{ROOT}/forecast/forecasts.csv"
FC_FIELDS = ["key", "batch", "made_at", "question", "close", "category", "my_prob",
             "saw_market_price", "reason", "mkt_bid", "mkt_ask", "mkt_mid", "fee_rate",
             "price_ts", "outcome", "resolved_at"]


def read_fc():
    if not os.path.exists(FC_PATH):
        return []
    return list(csv.DictReader(open(FC_PATH)))


def write_fc(rows):
    with open(FC_PATH, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FC_FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FC_FIELDS})
