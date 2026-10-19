# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-19T20:04:35Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-19T20:04:32Z — 249 of 249 pairs priced
- Scans in the last 24h: 39 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-19T18:59:24Z — Kalshi 121883 markets, Polymarket 20575 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 220 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 84
- Positive pairs still in play: **210** (confirmed same bet: 0, not yet checked: 207)
- Scans with at least one positive pair: 220

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXHIGHTSEA-26OCT18-B60.5 /  | no | +98.8¢ | +72.8¢ | 29 | 50 | 0 | >999% |
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | no | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| Highest temperature in Atlanta on Oct 19, 202 / Will the highest temperature in Atlanta be be | no | +78.9¢ | +13.0¢ | 31 | 50 | 1 | >999% |
| Highest temperature in Atlanta on Oct 19, 202 / Will the highest temperature in Atlanta be be | no | +72.6¢ | +16.1¢ | 37 | 50 | 1 | >999% |
| Highest temperature in Houston on Oct 19, 202 / Will the highest temperature in Houston be be | no | +71.9¢ | +15.5¢ | 39 | 50 | 1 | >999% |
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | no | +68.9¢ | +61.8¢ | 161 | 50 | 8 | >999% |
| Highest temperature in Houston on Oct 19, 202 / Will the highest temperature in Houston be be | no | +64.1¢ | +15.2¢ | 41 | 50 | 1 | >999% |
| KXHIGHTSEA-26OCT17-B60.5 /  | no | +51.7¢ | +6.2¢ | 16 | 46 | 1 | >999% |
| KXHIGHMIA-26OCT16-B88.5 /  | no | +48.2¢ | +25.6¢ | 37 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 4 run, 69 positive spreads seen; typical one lasted 1755 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 305. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: Detroit: Stage of Elimination — 6 outcomes, +4.0¢ per $1
  - kalshi: Pro Baseball Championship Series MVP Winner — 23 outcomes, +4.0¢ per $1
  - polymarket: Prime Minister of Israel after the next election? Benjamin Netanyahu — 13 outcomes, +4.0¢ per $1
  - polymarket: Victoria Parliamentary Election: 3rd Place Greens — 8 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Cape Town on October 20? 17°C — 3 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 20, settled: 3, still open: 19
- Accuracy score (lower is better): Claude 0.103, market 0.160 → so far Claude is more accurate; gap -0.057 (± 0.064). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 3 bets, $1.31 staked, result $+0.64 (+49%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
