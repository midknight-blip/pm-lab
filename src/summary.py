"""Rebuild README.md: a short plain-English status page. Runs after every scan."""
import csv, glob, json, os, statistics, sys
from collections import defaultdict
from datetime import timedelta
sys.path.insert(0, os.path.dirname(__file__))
from common import *  # noqa


def load_json(path, default=None):
    try:
        return json.load(open(path))
    except Exception:
        return default


def cents(x):
    return f"{x * 100:+.1f}¢"


def health_section():
    h = load_json(f"{ROOT}/arb/health.json", {})
    cat = load_json(f"{ROOT}/arb/catalog_stats.json", {})
    runs = list(csv.DictReader(open(f"{ROOT}/arb/runs.csv"))) if os.path.exists(f"{ROOT}/arb/runs.csv") else []
    cutoff = now() - timedelta(hours=24)
    last24 = [r for r in runs if parse_ts(r["ts"]) and parse_ts(r["ts"]) > cutoff]
    errs = sum(1 for r in last24 if r["error"])
    lines = ["## Health", "",
             f"- Last scan: {h.get('last_scan','never')} — {h.get('pairs_priced',0)} of {h.get('pairs_watched',0)} pairs priced"
             + (f" — **error:** `{h['error']}`" if h.get("error") else ""),
             f"- Scans in the last 24h: {len(last24)} (GitHub runs these roughly every 15 min; 60-96 is normal), errors: {errs}",
             f"- Last market list refresh: {cat.get('updated','never')} — Kalshi {cat.get('kalshi_markets','?')} markets, "
             f"Polymarket {cat.get('poly_markets_binary','?')} yes/no markets, {cat.get('pairs','?')} matched pairs", ""]
    return lines, runs


def arb_section(runs):
    pairs = {p["pair_id"]: p for p in (load_json(f"{ROOT}/arb/pairs_auto.json", {}) or {}).get("pairs", [])}
    review = load_json(f"{ROOT}/arb/pairs_review.json", {}) or {}
    rows = []
    for path in sorted(glob.glob(f"{ROOT}/arb/log/*.csv")):
        rows += list(csv.DictReader(open(path)))
    pos = [r for r in rows if float(r["net_edge"]) > 0]
    by_pair = defaultdict(list)
    for r in pos:
        by_pair[r["pair_id"]].append(r)
    first = runs[0]["ts"][:10] if runs else "—"
    lines = ["## Arbitrage test", "",
             f"Running since {first}. {len(runs)} scans so far. A pair counts as positive when buying both sides "
             "costs less than $1 after fees, at the best available price.", "",
             f"- Pairs that were ever positive: **{len(by_pair)}** "
             f"(confirmed same bet: {sum(1 for p in by_pair if review.get(p,{}).get('status')=='same')}, "
             f"not yet checked: {sum(1 for p in by_pair if p not in review)})",
             f"- Scans with at least one positive pair: {sum(1 for r in runs if r['n_positive'] not in ('', '0'))}", ""]
    if by_pair:
        lines += ["| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |",
                  "|---|---|---|---|---|---|---|---|"]
        ranked = sorted(by_pair.items(), key=lambda kv: max(float(r["net_edge"]) for r in kv[1]), reverse=True)[:10]
        for pid, rs in ranked:
            p = pairs.get(pid, {})
            name = (p.get("kalshi_text", pid.split("|")[0])[:45] + " / " + p.get("poly_text", "")[:45]).replace("|", "/")
            edges = [float(r["net_edge"]) for r in rs]
            lines.append(f"| {name} | {review.get(pid,{}).get('status','no')} | {cents(max(edges))} | "
                         f"{cents(statistics.median(edges))} | {len({r['ts'] for r in rs})} | "
                         f"{max(float(r['size']) for r in rs):.0f} | {float(rs[-1]['days']):.0f} | "
                         f"{max(float(r['annualized']) for r in rs) * 100:.0f}% |")
        lines.append("")
    lines += burst_lines() + bundle_lines() + [""]
    return lines


def burst_lines():
    files = sorted(glob.glob(f"{ROOT}/arb/burst/*.csv"))
    if not files:
        return ["- Fast-check sessions (every 15 sec): none yet"]
    durs, sessions = [], len(files)
    for path in files:
        series = defaultdict(list)
        for r in csv.DictReader(open(path)):
            series[(r["pair_id"], r["dir"])].append((parse_ts(r["ts"]), float(r["net_edge"])))
        for pts in series.values():
            pts.sort()
            start = None
            for i, (t, e) in enumerate(pts):
                if e > 0 and start is None:
                    start = t
                if (e <= 0 or i == len(pts) - 1) and start is not None:
                    end = t if e <= 0 else t + timedelta(seconds=15)
                    durs.append((end - start).total_seconds())
                    start = None
    if not durs:
        return [f"- Fast-check sessions (every 15 sec): {sessions} run, no positive spreads seen"]
    return [f"- Fast-check sessions (every 15 sec): {sessions} run, {len(durs)} positive spreads seen; "
            f"typical one lasted {statistics.median(durs):.0f} sec, longest {max(durs)/60:.1f} min"]


def bundle_lines():
    cutoff = now() - timedelta(days=3)
    best = {}
    for path in sorted(glob.glob(f"{ROOT}/arb/bundles/*.csv"))[-4:]:
        for r in csv.DictReader(open(path)):
            if parse_ts(r["ts"]) and parse_ts(r["ts"]) > cutoff and float(r["net_edge"]) > 0:
                k = (r["site"], r["event"])
                if k not in best or float(r["net_edge"]) > float(best[k]["net_edge"]):
                    best[k] = r
    if not best:
        return ["- Same-site bundles (buy every outcome of one event for under $1): none in the last 3 days"]
    top = sorted(best.values(), key=lambda r: float(r["net_edge"]), reverse=True)[:5]
    out = [f"- Same-site bundles in the last 3 days: {len(best)}. These only work if the listed outcomes "
           "cover every possibility, which still needs checking. Top ones:"]
    for r in top:
        out.append(f"  - {r['site']}: {r['title'][:70]} — {r['n_outcomes']} outcomes, {cents(float(r['net_edge']))} per $1")
    return out


def forecast_section():
    s = load_json(f"{ROOT}/forecast/scores.json")
    lines = ["## Forecast test", ""]
    if not s:
        return lines + ["No forecasts yet. First batch comes at the next Monday/Thursday check-in.", ""]
    a = s["all"]
    lines.append(f"- Forecasts made: {s['forecasts_made']}, settled: {a.get('n',0)}, still open: {s['pending']}")
    if a.get("n"):
        verdict = "Claude is more accurate" if a["claude_minus_market"] < 0 else "the market is more accurate"
        se = f" (± {a['std_error']:.3f})" if a.get("std_error") else ""
        lines += [f"- Accuracy score (lower is better): Claude {a['brier_claude']:.3f}, market {a['brier_market']:.3f} "
                  f"→ so far {verdict}; gap {a['claude_minus_market']:+.3f}{se}. "
                  "Needs ~100 settled before this means much.",
                  f"- Paper bets (when Claude disagreed by 5+ points): {a['paper_bets']} bets, "
                  f"${a['paper_staked']:.2f} staked, result ${a['paper_pnl']:+.2f}"
                  + (f" ({a['paper_roi']*100:+.0f}%)" if a.get("paper_roi") is not None else "")]
    return lines + [""]


def main():
    h, runs = health_section()
    body = ["# pm-lab", "",
            "Read-only test of two ideas on Kalshi and Polymarket. No money is involved. "
            f"Updated automatically — last update {iso()}.", "",
            "1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?",
            "2. **Forecasting:** can Claude's researched probabilities beat the market price?", ""]
    body += h + arb_section(runs) + forecast_section()
    body += ["---", "How it works: `src/` has the code, `arb/` and `forecast/` hold the data. "
             "See `CHECKIN.md` for what the twice-weekly Claude check-in does."]
    with open(f"{ROOT}/README.md", "w") as fh:
        fh.write("\n".join(body) + "\n")


if __name__ == "__main__":
    main()
