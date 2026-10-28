"""A few times a week: watch the closest pairs every 15 seconds for ~2 hours
to see how long any positive spread actually lasts.

Writes arb/burst/DATE-HHMM.csv
"""
import csv, glob, os, sys, time
sys.path.insert(0, os.path.dirname(__file__))
from common import *  # noqa
from scan import load_pairs, snapshot, append

MINUTES = int(os.environ.get("BURST_MINUTES", "120"))
EVERY = 15
TOP = 12


def closest_pairs(pairs):
    """Pairs whose best recent net edge was highest (closest to an arb)."""
    logs = sorted(glob.glob(f"{ROOT}/arb/log/*.csv"))[-2:]
    best = {}
    for path in logs:
        for r in csv.DictReader(open(path)):
            e = float(r["net_edge"])
            if e >= 0.15:  # implausibly large: a rules gap or a frozen price, not worth watching
                continue
            if e > best.get(r["pair_id"], -9):
                best[r["pair_id"]] = e
    ranked = sorted(pairs, key=lambda p: best.get(p["pair_id"], -9), reverse=True)
    return ranked[:TOP]


def main():
    pairs = closest_pairs(load_pairs())
    start = now()
    path = f"{ROOT}/arb/burst/{start:%Y-%m-%d-%H%M}.csv"
    end = time.time() + MINUTES * 60
    while time.time() < end:
        t = time.time()
        try:
            _, rows, _ = snapshot(pairs)
            append(path, rows)
        except Exception as e:
            print("poll failed", e)
        time.sleep(max(0, EVERY - (time.time() - t)))
    print("burst done", path)


if __name__ == "__main__":
    main()
