# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-18T17:18:48Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-18T17:18:44Z — 238 of 249 pairs priced
- Scans in the last 24h: 47 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-18T12:52:34Z — Kalshi 134104 markets, Polymarket 20541 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 176 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 76
- Positive pairs still in play: **170** (confirmed same bet: 0, not yet checked: 167)
- Scans with at least one positive pair: 176

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXHIGHAUS-26OCT17-B70.5 /  | no | +98.8¢ | +28.3¢ | 25 | 50 | 1 | >999% |
| KXHIGHAUS-26OCT17-B68.5 /  | no | +98.8¢ | +30.5¢ | 25 | 50 | 1 | >999% |
| KXHIGHMIA-26OCT17-B88.5 /  | no | +98.8¢ | +98.2¢ | 23 | 50 | 1 | >999% |
| KXHIGHMIA-26OCT17-B90.5 /  | no | +98.8¢ | +98.4¢ | 25 | 50 | 1 | >999% |
| KXHIGHLAX-26OCT17-B88.5 /  | no | +98.8¢ | +56.6¢ | 20 | 50 | 0 | >999% |
| KXHIGHLAX-26OCT17-B90.5 /  | no | +98.8¢ | +63.1¢ | 19 | 50 | 0 | >999% |
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | no | +63.8¢ | +61.8¢ | 117 | 50 | 10 | >999% |
| KXHIGHTSEA-26OCT17-B60.5 /  | no | +51.7¢ | +6.2¢ | 16 | 46 | 1 | >999% |
| KXHIGHMIA-26OCT16-B88.5 /  | no | +48.2¢ | +25.6¢ | 37 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 3 run, 44 positive spreads seen; typical one lasted 2002 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 316. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: Detroit: Stage of Elimination — 6 outcomes, +4.0¢ per $1
  - polymarket: Prime Minister of Israel after the next election? Benjamin Netanyahu — 13 outcomes, +4.0¢ per $1
  - kalshi: Arizona State Senate winner? — 2 outcomes, +4.0¢ per $1
  - kalshi: Pro Baseball Championship Series MVP Winner — 23 outcomes, +4.0¢ per $1
  - polymarket: Who will be UFC Lightweight champion at the end of 2026? Justin Gaethj — 2 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 10, settled: 1, still open: 10
- Accuracy score (lower is better): Claude 0.062, market 0.212 → so far Claude is more accurate; gap -0.149. Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 1 bets, $0.57 staked, result $+0.41 (+72%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
