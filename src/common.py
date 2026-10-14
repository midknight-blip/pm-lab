"""Shared helpers: HTTP, the two public APIs, fees, and text matching.

Stdlib only, so the GitHub Actions jobs need no installs.
"""
import json, math, os, re, time, urllib.request, urllib.error
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KALSHI = "https://api.elections.kalshi.com/trade-api/v2"
GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
UA = {"User-Agent": "pm-lab/0.2 (research, read-only)", "Accept": "application/json"}

KALSHI_FEE_RATE = 0.07  # general schedule; some index products differ


def now():
    return datetime.now(timezone.utc)


def iso(dt=None):
    return (dt or now()).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_ts(s):
    if not s:
        return None
    try:
        s = s.replace("Z", "+00:00")
        if "." in s:  # trim fractional seconds to 6 digits for fromisoformat
            head, rest = s.split(".", 1)
            frac = re.match(r"\d+", rest).group(0)
            s = head + "." + frac[:6].ljust(6, "0") + rest[len(frac):]
        dt = datetime.fromisoformat(s)
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def http(url, body=None, tries=4):
    data = None
    headers = dict(UA)
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(2 ** i)
                continue
            raise
        except Exception:
            if i < tries - 1:
                time.sleep(2 ** i)
                continue
            raise


def f(x, default=None):
    try:
        if x is None or x == "":
            return default
        return float(x)
    except Exception:
        return default


# ---------------------------------------------------------------- fees
def kalshi_fee(price, n):
    """Taker fee in dollars for n contracts at price, rounded up to the cent."""
    if n <= 0:
        return 0.0
    return math.ceil(KALSHI_FEE_RATE * n * price * (1 - price) * 100 - 1e-9) / 100


def poly_fee(price, n, rate):
    """Polymarket taker fee: C * rate * p * (1-p). rate=0 for fee-free markets."""
    return round(n * (rate or 0) * price * (1 - price), 5)


# ---------------------------------------------------------------- Kalshi
def kalshi_open_events(max_pages=150):
    """All open Kalshi events with nested markets, skipping multi-leg parlays."""
    out, cursor = [], None
    for _ in range(max_pages):
        url = f"{KALSHI}/events?status=open&with_nested_markets=true&limit=200"
        if cursor:
            url += f"&cursor={cursor}"
        d = http(url)
        for e in d.get("events", []):
            if e.get("event_ticker", "").startswith("KXMVE"):
                continue
            out.append(e)
        cursor = d.get("cursor")
        if not cursor:
            break
        time.sleep(0.15)
    return out


def kalshi_markets_by_ticker(tickers):
    res = {}
    tickers = list(tickers)
    for i in range(0, len(tickers), 50):
        chunk = tickers[i:i + 50]
        d = http(f"{KALSHI}/markets?tickers={','.join(chunk)}&limit=100")
        for m in d.get("markets", []):
            res[m["ticker"]] = m
        time.sleep(0.15)
    return res


def kalshi_market(ticker):
    return http(f"{KALSHI}/markets/{ticker}").get("market", {})


def kalshi_quote(m):
    """Top of book from a Kalshi market object. Asks on each side + sizes."""
    yb, ya = f(m.get("yes_bid_dollars")), f(m.get("yes_ask_dollars"))
    nb, na = f(m.get("no_bid_dollars")), f(m.get("no_ask_dollars"))
    if na is None and yb is not None:
        na = round(1 - yb, 4)
    if ya is None and nb is not None:
        ya = round(1 - nb, 4)
    return {
        "yes_bid": yb, "yes_ask": ya, "no_ask": na,
        "yes_ask_size": f(m.get("yes_ask_size_fp"), 0.0),
        # size available to buy NO at no_ask = size resting on the YES bid
        "no_ask_size": f(m.get("yes_bid_size_fp"), 0.0),
    }


# ---------------------------------------------------------------- Polymarket
POLY_PAGING_NOTE = {}


def poly_open_markets(max_pages=40):
    out = []
    """The API refuses offsets past ~2,000, so query one settlement week at a
    time (most liquid first) and merge."""
    from datetime import timedelta
    seen, capped = {}, 0
    start = now() - timedelta(days=2)
    windows = [(start + timedelta(days=7 * i), start + timedelta(days=7 * (i + 1))) for i in range(27)]
    windows.append((start + timedelta(days=189), start + timedelta(days=3650)))
    for lo, hi in windows:
        offset = 0
        for _ in range(max_pages):
            url = (f"{GAMMA}/markets?active=true&closed=false&archived=false&limit=500"
                   f"&order=volume24hr&ascending=false&end_date_min={iso(lo)}&end_date_max={iso(hi)}"
                   f"&offset={offset}")
            try:
                d = http(url)
            except Exception:
                capped += 1  # deep page refused; the least-traded markets are missed
                break
            if not d:
                break
            for m in d:
                seen[str(m.get("id"))] = m
            offset += len(d)
            if len(d) < 100:
                break
            time.sleep(0.1)
    POLY_PAGING_NOTE["stopped"] = f"{capped} weekly windows hit the page limit" if capped else "complete"
    return list(seen.values())


def poly_is_binary_yes_no(m):
    try:
        outs = json.loads(m.get("outcomes") or "[]")
        toks = json.loads(m.get("clobTokenIds") or "[]")
    except Exception:
        return False
    return ([o.lower() for o in outs] == ["yes", "no"] and len(toks) == 2
            and m.get("enableOrderBook") and m.get("acceptingOrders", True))


def poly_yes_token(m):
    return json.loads(m["clobTokenIds"])[0]


def poly_fee_rate(m):
    if not m.get("feesEnabled"):
        return 0.0
    fs = m.get("feeSchedule") or {}
    return f(fs.get("rate"), 0.0)


def poly_books(token_ids):
    """Order books for many tokens. Returns {token_id: book}."""
    res = {}
    token_ids = list(token_ids)
    for i in range(0, len(token_ids), 100):
        chunk = token_ids[i:i + 100]
        try:
            d = http(f"{CLOB}/books", body=[{"token_id": t} for t in chunk])
            for b in d:
                res[b.get("asset_id")] = b
        except Exception:
            for t in chunk:  # fall back to one at a time
                try:
                    res[t] = http(f"{CLOB}/book?token_id={t}")
                except Exception:
                    pass
        time.sleep(0.15)
    return res


def poly_quote(book):
    """YES ask/bid and sizes from the YES token book. NO ask = 1 - YES bid."""
    bids = [(f(b["price"]), f(b["size"])) for b in book.get("bids", [])]
    asks = [(f(a["price"]), f(a["size"])) for a in book.get("asks", [])]
    yb = max(bids, default=(None, 0))
    ya = min(asks, default=(None, 0))
    return {
        "yes_bid": yb[0], "yes_ask": ya[0],
        "no_ask": round(1 - yb[0], 4) if yb[0] is not None else None,
        "yes_ask_size": ya[1], "no_ask_size": yb[1],
    }


# ---------------------------------------------------------------- matching
STOP = set("""will the a an be by on in of to for at and or is are does do did
than this that with from after before end any as its it who what which when
win wins winning market yes no fc cf sc afc ac club vs v versus game match
""".split())
MONTHS = ("january february march april may june july august september october "
          "november december jan feb mar apr jun jul aug sep sept oct nov dec").split()


def norm_num(tok):
    m = re.fullmatch(r"\$?(\d+(?:\.\d+)?)(k|m|b|bn|%|bps)?", tok)
    if not m:
        return None
    v = float(m.group(1))
    mult = {"k": 1e3, "m": 1e6, "b": 1e9, "bn": 1e9}.get(m.group(2) or "", 1)
    v *= mult
    return ("%g" % v)


SYN = {"hike": "increase", "hikes": "increase", "raise": "increase", "raises": "increase",
       "increases": "increase", "cut": "decrease", "cuts": "decrease", "lower": "decrease",
       "lowers": "decrease", "decreases": "decrease", "maintain": "hold", "maintains": "hold",
       "holds": "hold", "unchanged": "hold", "pause": "hold", "change": "hold", "tie": "draw",
       "republican": "gop", "republicans": "gop", "democrat": "dem", "democrats": "dem",
       "democratic": "dem", "btc": "bitcoin", "eth": "ethereum", "us": "usa", "u.s": "usa",
       "vp": "vice", "nomination": "nominee", "nominated": "nominee", "1h": "half", "2h": "half",
       "1st": "first", "president": "presidential", "presidency": "presidential", "above": "over", "greater": "over", "below": "under", "less": "under"}
# Words that change what the bet is about. If one side has one of these and the
# other doesn't, they're different bets (VP vs President, nominee vs winner, 1st half vs full game).
CRITICAL = {"vice", "nominee", "primary", "runoff", "matchup", "popular", "electoral", "margin",
            "half", "quarter", "period", "inning", "innings", "spread", "total", "map", "set",
            "round", "overtime", "dem", "gop", "independent", "senate", "house", "governor",
            "mayor", "speaker", "seats", "majority", "control", "first", "exact",
            "monthly", "weekly", "annual", "yearly", "high", "low", "over", "under",
            "album", "song", "single", "plus", "tweet", "tweets", "post", "posts"}
# Words that say nothing about the subject; a pair must share at least one word outside this set.
GENERIC = {"over", "under", "increase", "decrease", "hold", "high", "low", "first", "new", "get",
           "usa", "election", "winner", "price", "rate", "rates", "reach", "hit", "dip", "say",
           "announce", "release", "year", "day", "week", "month", "official", "officially", "leader",
           "presidential", "trump", "donald", "next", "least", "more", "most", "many", "much"}
UNITS = {"bps", "bp", "pts", "points", "percent", "basis"}


def tokens(text):
    t = text.lower()
    t = re.sub(r"\b20\d\d-\d\d-\d\d\b", " ", t)  # iso dates
    mon = "|".join(MONTHS)
    t = re.sub(rf"\b({mon})\.?\s+\d{{1,2}}(st|nd|rd|th)?\b", r" \1 ", t)  # "Oct 15" -> "oct"
    t = re.sub(rf"\b\d{{1,2}}(st|nd|rd|th)?\s+({mon})\b", r" \2 ", t)        # "15 October"
    t = re.sub(r"\b\d{1,2}/\d{1,2}(/\d{2,4})?\b", " ", t)                       # 10/15
    t = t.replace(">", " over ").replace("<", " under ").replace("+", " plus ")
    t = re.sub(r"(\d),(\d{3})", r"\1\2", t)       # 150,000 -> 150000
    t = re.sub(r"[^a-z0-9.$%]+", " ", t)
    words, nums = set(), set()
    for w in t.split():
        w = w.strip(".")
        if not w or w in STOP or w in MONTHS:
            continue
        n = norm_num(w)
        if n is not None:
            if re.fullmatch(r"20[2-3]\d", w):  # a year
                continue
            nums.add(n)
        elif len(w) > 1 and w not in UNITS:
            words.add(SYN.get(w, w))
    return words, nums
