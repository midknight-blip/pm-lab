# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-17T01:00:02Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-17T00:39:53Z — 240 of 249 pairs priced
- Scans in the last 24h: 41 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-17T01:00:02Z — Kalshi 150001 markets, Polymarket 21229 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 97 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 76
- Positive pairs still in play: **113** (confirmed same bet: 0, not yet checked: 110)
- Scans with at least one positive pair: 97

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | no | +61.8¢ | +49.7¢ | 61 | 50 | 11 | >999% |
| KXHIGHMIA-26OCT16-B88.5 /  | no | +48.2¢ | +25.6¢ | 37 | 50 | 1 | >999% |
| KXHIGHMIA-26OCT16-B90.5 /  | no | +40.9¢ | +22.8¢ | 38 | 50 | 1 | >999% |
| KXHIGHAUS-26OCT17-B68.5 /  | no | +36.6¢ | +26.9¢ | 12 | 44 | 2 | >999% |
| KXHIGHAUS-26OCT17-B70.5 /  | no | +30.3¢ | +22.6¢ | 12 | 50 | 2 | >999% |
| KXHIGHTDAL-26OCT16-B68.5 /  | no | +27.8¢ | +9.2¢ | 31 | 50 | 1 | >999% |
| KXHIGHTDAL-26OCT16-B70.5 /  | no | +23.6¢ | +16.4¢ | 20 | 50 | 1 | >999% |
| KXHIGHTSFO-26OCT16-B84.5 /  | no | +22.0¢ | +7.7¢ | 42 | 50 | 1 | >999% |
| KXHIGHTSFO-26OCT16-B88.5 /  | no | +20.5¢ | +8.3¢ | 43 | 50 | 1 | >999% |
| Athletic vs Valencia Athletic / Will Athletic Club win on 2026-10-17? | no | +19.2¢ | +16.6¢ | 24 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 2 run, 39 positive spreads seen; typical one lasted 885 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 332. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: Arizona State Senate winner? — 2 outcomes, +4.0¢ per $1
  - kalshi: Detroit: Stage of Elimination — 6 outcomes, +4.0¢ per $1
  - polymarket: NM-03 House Election Margin of Victory Democrat 20-25% — 2 outcomes, +4.0¢ per $1
  - polymarket: Third-best AI Lab end of December? Alibaba — 18 outcomes, +4.0¢ per $1
  - polymarket: Who will be UFC Lightweight champion at the end of 2026? Justin Gaethj — 2 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 10, settled: 0, still open: 10

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
