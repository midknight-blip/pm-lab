# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-19T22:22:43Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-19T22:22:40Z — 239 of 249 pairs priced
- Scans in the last 24h: 38 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-19T18:59:24Z — Kalshi 121883 markets, Polymarket 20575 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 224 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 84
- Positive pairs still in play: **212** (confirmed same bet: 0, not yet checked: 209)
- Scans with at least one positive pair: 224

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXHIGHTSEA-26OCT18-B60.5 /  | no | +98.8¢ | +72.8¢ | 29 | 50 | 0 | >999% |
| Highest temperature in Houston on Oct 19, 202 / Will the highest temperature in Houston be be | no | +98.7¢ | +16.1¢ | 45 | 50 | 1 | >999% |
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| Highest temperature in Houston on Oct 19, 202 / Will the highest temperature in Houston be be | no | +98.3¢ | +15.8¢ | 43 | 50 | 1 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | no | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| Highest temperature in Atlanta on Oct 19, 202 / Will the highest temperature in Atlanta be be | no | +78.9¢ | +16.4¢ | 35 | 50 | 1 | >999% |
| Highest temperature in Atlanta on Oct 19, 202 / Will the highest temperature in Atlanta be be | no | +75.6¢ | +16.1¢ | 41 | 50 | 1 | >999% |
| Highest temperature in Austin on Oct 19, 2026 / Will the highest temperature in Austin be bet | no | +73.2¢ | +14.0¢ | 45 | 50 | 1 | >999% |
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | no | +68.9¢ | +61.8¢ | 165 | 50 | 8 | >999% |
| Highest temperature in Austin on Oct 19, 2026 / Will the highest temperature in Austin be bet | no | +68.9¢ | +5.0¢ | 25 | 50 | 1 | >999% |

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
