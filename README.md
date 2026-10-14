# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-14T17:49:37Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-14T17:48:37Z — 250 of 250 pairs priced
- Scans in the last 24h: 3 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-14T17:48:10Z — Kalshi 133183 markets, Polymarket 21304 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 3 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 71
- Positive pairs still in play: **14** (confirmed same bet: 0, not yet checked: 14)
- Scans with at least one positive pair: 3

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Top 5 most searched people on Google in 2026  / Will Lindsay Clancy rank in Google’s Top 5 Mo | no | +6.3¢ | +6.3¢ | 2 | 50 | 78 | 31% |
| Top 5 most searched people on Google in 2026  / Will Nicolás Maduro rank in Google’s Top 5 Mo | no | +2.2¢ | +2.2¢ | 2 | 5 | 78 | 11% |
| Copa do Brasil Champion Palmeiras / Will Palmeiras win the 2026 Copa do Brasil? | no | +1.8¢ | +1.8¢ | 2 | 1 | 53 | 12% |
| Time's Person of the Year for 2026 Bernie San / Will Bernie Sanders be TIME Person of the Yea | no | +1.8¢ | +1.8¢ | 2 | 50 | 79 | 8% |
| Time's Person of the Year for 2026 Marco Rubi / Will Marco Rubio be TIME Person of the Year 2 | no | +1.2¢ | +1.2¢ | 2 | 40 | 79 | 5% |
| Texas State Senate winner? Republican party / Will the Republican Party control the Texas S | no | +1.1¢ | +1.1¢ | 2 | 50 | 20 | 20% |
| MotoGP World Champion Marco Bezzecchi / Will Marco Bezzecchi win the 2026 MotoGP Worl | no | +1.1¢ | +1.1¢ | 2 | 2 | 47 | 9% |
| Time's Person of the Year for 2026 James Tala / Will James Talarico be TIME Person of the Yea | no | +0.9¢ | +0.9¢ | 2 | 20 | 79 | 4% |
| Fed decision in Jan 2027? Cut 25bps / Will the Fed decrease interest rates by 25 bp | no | +0.5¢ | +0.5¢ | 2 | 50 | 105 | 2% |
| Game Awards: Best Multiplayer Marathon / Will Marathon win Best Multiplayer at the 202 | no | +0.5¢ | +0.5¢ | 2 | 5 | 78 | 2% |

- Fast-check sessions (every 15 sec): none yet
- Same-site bundles (buy every outcome of one event for under $1): none in the last 3 days

## Forecast test

No forecasts yet. First batch comes at the next Monday/Thursday check-in.

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
