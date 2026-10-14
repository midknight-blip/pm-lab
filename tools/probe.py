"""Save small raw samples from both public APIs so field names can be checked."""
import json, os, urllib.request

OUT = "probe"
os.makedirs(OUT, exist_ok=True)

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "pm-lab/0.1", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())

def save(name, url):
    try:
        data = get(url)
    except Exception as e:  # keep going, record the error
        data = {"_error": repr(e), "_url": url}
    with open(f"{OUT}/{name}.json", "w") as f:
        json.dump(data, f, indent=1)
    return data

K = "https://api.elections.kalshi.com/trade-api/v2"
km = save("kalshi_markets", f"{K}/markets?status=open&limit=5")
save("kalshi_events", f"{K}/events?status=open&limit=3&with_nested_markets=true")
try:
    t = km["markets"][0]["ticker"]
    save("kalshi_orderbook", f"{K}/markets/{t}/orderbook")
except Exception as e:
    print("kalshi ob skipped", e)
save("kalshi_series", f"{K}/series?limit=3")

G = "https://gamma-api.polymarket.com"
pm = save("poly_markets", f"{G}/markets?active=true&closed=false&limit=5&order=volume24hr&ascending=false")
save("poly_events", f"{G}/events?active=true&closed=false&limit=2&order=volume24hr&ascending=false")
try:
    tok = json.loads(pm[0]["clobTokenIds"])[0]
    save("poly_book", f"https://clob.polymarket.com/book?token_id={tok}")
except Exception as e:
    print("poly book skipped", e)
print("done")
