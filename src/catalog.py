"""Every 6 hours: pull both full market lists, match equivalent markets,
and look for single-site bundles (all outcomes of one event priced under $1).

Writes:
  arb/pairs_auto.json   matched Kalshi <-> Polymarket pairs the 15-min scan watches
  arb/bundles/DATE.csv  single-site bundle candidates (appended)
  arb/catalog_stats.json
"""
import csv, json, math, os, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from common import *  # noqa

MAX_PAIRS = 250
MIN_SCORE = 0.45
MAX_CLOSE_GAP_DAYS = 4
MAX_DAYS_OUT = 180  # money locked up longer than this isn't worth it for a small account


def kalshi_rows(events):
    rows = []
    for e in events:
        for m in e.get("markets", []):
            if m.get("status") not in ("active", "open"):
                continue
            close = parse_ts(m.get("expected_expiration_time")) or parse_ts(m.get("close_time"))
            sub = m.get("yes_sub_title") or ""
            text = f"{e.get('title','')} {sub}"
            rows.append({"subject": sub,
                "ticker": m["ticker"], "event": e["event_ticker"], "text": text.strip(),
                "category": e.get("category"), "close": close,
                "rules": (m.get("rules_primary") or "")[:700],
                "vol24": f(m.get("volume_24h_fp"), 0), "q": kalshi_quote(m),
            })
    return rows


def poly_rows(markets):
    rows = []
    for m in markets:
        if not poly_is_binary_yes_no(m):
            continue
        ev = (m.get("events") or [{}])[0].get("title") or ""
        sub = m.get("groupItemTitle") or ""
        rows.append({
            "subject": sub, "id": str(m["id"]),
            "text": f"{ev} {sub or m.get('question', '')}".strip(), "question": m.get("question", ""), "close": parse_ts(m.get("endDate")),
            "token": poly_yes_token(m), "fee_rate": poly_fee_rate(m),
            "rules": (m.get("description") or "")[:700], "slug": m.get("slug"),
            "vol24": f(m.get("volume24hr"), 0), "neg_risk_id": m.get("negRiskMarketID"),
            "best_ask": f(m.get("bestAsk")), "best_bid": f(m.get("bestBid")),
        })
    return rows


def match(krows, prows):
    ktoks = [tokens(r["text"]) for r in krows]
    ptoks = [tokens(r["text"]) for r in prows]
    kdate = [dates(r["text"] + " " + r.get("ticker", "")) for r in krows]
    pdate = [dates(r["text"] + " " + r.get("question", "")) for r in prows]
    ksub = [tokens(r["subject"])[0] for r in krows]
    psub = [tokens(r["subject"])[0] for r in prows]
    df = defaultdict(int)
    for w, _ in ktoks + ptoks:
        for t in w:
            df[t] += 1
    n = len(ktoks) + len(ptoks)
    idf = {t: math.log(n / c) for t, c in df.items()}
    index = defaultdict(list)
    for i, (w, _) in enumerate(ktoks):
        for t in w:
            if df[t] < 3000:
                index[t].append(i)

    best_for_k = {}
    for j, (pw, pn) in enumerate(ptoks):
        p = prows[j]
        if not pw or p["close"] is None or (p["close"] - now()).days > MAX_DAYS_OUT:
            continue
        hits = defaultdict(int)
        for t in pw:
            for i in index.get(t, ()):
                hits[i] += 1
        best = None
        for i, c in hits.items():
            if c < (2 if len(pw) > 2 else 1):
                continue
            k = krows[i]
            if k["close"] is None or abs((k["close"] - p["close"]).total_seconds()) > MAX_CLOSE_GAP_DAYS * 86400:
                continue
            if (k["close"] - now()).days > MAX_DAYS_OUT:
                continue
            kw, kn = ktoks[i]
            if kdate[i] and pdate[j] and not (kdate[i] & pdate[j]):
                continue  # different days
            if (kw ^ pw) & CRITICAL:
                continue
            if kn and pn and kn != pn:
                continue  # different thresholds/numbers -> different bet
            if not ((kw & pw) - GENERIC):
                continue  # only "below" + a number in common -> different subjects
            inter = sum(idf[t] for t in kw & pw)
            union = sum(idf[t] for t in kw | pw)
            s = inter / union if union else 0
            if kn and pn:
                s += 0.1
            if ksub[i] and psub[j]:  # e.g. which team / which candidate
                if not (ksub[i] & psub[j]):
                    continue
                s += 0.2
            if s >= MIN_SCORE and (best is None or s > best[0]):
                best = (s, i)
        if best:
            s, i = best
            if i not in best_for_k or s > best_for_k[i][0]:
                best_for_k[i] = (s, j)

    pairs = []
    for i, (s, j) in best_for_k.items():
        k, p = krows[i], prows[j]
        pairs.append({
            "pair_id": f"{k['ticker']}|{p['id']}", "score": round(s, 3),
            "kalshi_ticker": k["ticker"], "kalshi_text": k["text"], "kalshi_rules": k["rules"],
            "kalshi_close": iso(k["close"]), "category": k["category"],
            "poly_id": p["id"], "poly_slug": p["slug"], "poly_text": p["question"], "poly_rules": p["rules"],
            "poly_close": iso(p["close"]), "poly_token": p["token"], "poly_fee_rate": p["fee_rate"],
            "vol24": round(k["vol24"] + p["vol24"], 2),
        })
    pairs.sort(key=lambda r: (r["score"], r["vol24"]), reverse=True)
    return pairs[:MAX_PAIRS]


def bundles(events, prows):
    """Events where buying YES on every outcome costs under $1 (before checking
    that the outcomes really cover every possibility)."""
    out = []
    for e in events:
        if not e.get("mutually_exclusive"):
            continue
        ms = [m for m in e.get("markets", []) if m.get("status") in ("active", "open")]
        if len(ms) < 2:
            continue
        qs = [kalshi_quote(m) for m in ms]
        if any(q["yes_ask"] is None or q["yes_ask"] >= 1 for q in qs):
            continue
        cost = sum(q["yes_ask"] for q in qs)
        fees = sum(kalshi_fee(q["yes_ask"], 10) / 10 for q in qs)  # per contract, buying 10
        size = min(q["yes_ask_size"] for q in qs)
        close = max((parse_ts(m.get("expected_expiration_time")) or parse_ts(m.get("close_time")) or now()) for m in ms)
        if 0.96 <= cost + fees < 0.995 and close and (close - now()).days <= MAX_DAYS_OUT:  # far under $1 = list clearly incomplete
            out.append(["kalshi", e["event_ticker"], e.get("title", "")[:120], len(ms),
                        round(cost, 4), round(fees, 4), round(1 - cost - fees, 4), size, iso(close)])
    groups = defaultdict(list)
    for p in prows:
        if p["neg_risk_id"]:
            groups[p["neg_risk_id"]].append(p)
    for gid, ps in groups.items():
        if len(ps) < 2 or any(p["best_ask"] is None for p in ps):
            continue
        cost = sum(p["best_ask"] for p in ps)
        fees = sum(poly_fee(p["best_ask"], 1, p["fee_rate"]) for p in ps)
        close = max(p["close"] for p in ps if p["close"]) if any(p["close"] for p in ps) else None
        if 0.96 <= cost + fees < 0.995 and close and (close - now()).days <= MAX_DAYS_OUT:
            out.append(["polymarket", gid, ps[0]["text"][:120], len(ps), round(cost, 4),
                        round(fees, 4), round(1 - cost - fees, 4), "", iso(close) if close else ""])
    return out


def main():
    t0 = now()
    try:
        _main(t0)
    except Exception as e:  # leave a trace in the repo, since Actions logs need a login
        import traceback
        with open(f"{ROOT}/arb/catalog_error.txt", "w") as fh:
            fh.write(iso() + "\n" + traceback.format_exc())
        raise


def _main(t0):
    events = kalshi_open_events()
    pmk = poly_open_markets()
    krows, prows = kalshi_rows(events), poly_rows(pmk)
    pairs = match(krows, prows)
    os.makedirs(f"{ROOT}/arb/bundles", exist_ok=True)
    with open(f"{ROOT}/arb/pairs_auto.json", "w") as fh:
        json.dump({"updated": iso(), "pairs": pairs}, fh, indent=1)
    b = bundles(events, prows)
    path = f"{ROOT}/arb/bundles/{t0:%Y-%m-%d}.csv"
    new = not os.path.exists(path)
    with open(path, "a", newline="") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["ts", "site", "event", "title", "n_outcomes", "cost", "fees", "net_edge", "min_size", "close"])
        for row in b:
            w.writerow([iso(t0)] + row)
    stats = {"updated": iso(), "kalshi_events": len(events), "kalshi_markets": len(krows),
             "poly_markets_binary": len(prows), "poly_markets_all": len(pmk),
             "pairs": len(pairs), "bundles_found": len(b),
             "poly_paging": POLY_PAGING_NOTE.get("stopped", "complete"),
             "seconds": round((now() - t0).total_seconds())}
    with open(f"{ROOT}/arb/catalog_stats.json", "w") as fh:
        json.dump(stats, fh, indent=1)
    print(json.dumps(stats))


if __name__ == "__main__":
    main()
