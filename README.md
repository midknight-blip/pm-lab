# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-14T17:09:57Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: never — 0 of 0 pairs priced
- Scans in the last 24h: 0 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: never — Kalshi ? markets, Polymarket ? yes/no markets, ? matched pairs

## Arbitrage test

Running since —. 0 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Pairs that were ever positive: **0** (confirmed same bet: 0, not yet checked: 0)
- Scans with at least one positive pair: 0

- Fast-check sessions (every 15 sec): none yet
- Same-site bundles (buy every outcome of one event for under $1): none in the last 3 days

## Forecast test

No forecasts yet. First batch comes at the next Monday/Thursday check-in.

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
