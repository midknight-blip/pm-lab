# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-17T20:53:16Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-17T20:53:14Z — 249 of 249 pairs priced
- Scans in the last 24h: 47 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-17T18:47:46Z — Kalshi 147483 markets, Polymarket 20647 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 136 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 76
- Positive pairs still in play: **137** (confirmed same bet: 0, not yet checked: 134)
- Scans with at least one positive pair: 136

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Highest temperature in Miami on Oct 17, 2026? / Will the highest temperature in Miami be betw | no | +98.8¢ | +6.1¢ | 15 | 50 | 1 | >999% |
| Highest temperature in Miami on Oct 17, 2026? / Will the highest temperature in Miami be betw | no | +98.8¢ | +11.2¢ | 17 | 50 | 1 | >999% |
| Highest temperature in Los Angeles on Oct 17, / Will the highest temperature in Los Angeles b | no | +65.7¢ | +12.0¢ | 10 | 50 | 1 | >999% |
| Highest temperature in Los Angeles on Oct 17, / Will the highest temperature in Los Angeles b | no | +63.1¢ | +2.4¢ | 9 | 43 | 1 | >999% |
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | no | +61.8¢ | +53.7¢ | 77 | 50 | 10 | >999% |
| KXHIGHMIA-26OCT16-B88.5 /  | no | +48.2¢ | +25.6¢ | 37 | 50 | 1 | >999% |
| Highest temperature in Seattle on Oct 17, 202 / Will the highest temperature in Seattle be be | no | +47.7¢ | +6.2¢ | 14 | 46 | 1 | >999% |
| Highest temperature in Austin on Oct 17, 2026 / Will the highest temperature in Austin be bet | no | +42.6¢ | +27.4¢ | 17 | 44 | 1 | >999% |
| KXHIGHMIA-26OCT16-B90.5 /  | no | +40.9¢ | +22.8¢ | 38 | 50 | 1 | >999% |
| Highest temperature in Austin on Oct 17, 2026 / Will the highest temperature in Austin be bet | no | +40.8¢ | +23.1¢ | 17 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 3 run, 44 positive spreads seen; typical one lasted 2002 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 343. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: Detroit: Stage of Elimination — 6 outcomes, +4.0¢ per $1
  - polymarket: Prime Minister of Israel after the next election? Benjamin Netanyahu — 13 outcomes, +4.0¢ per $1
  - polymarket: NM-03 House Election Margin of Victory Democrat 20-25% — 2 outcomes, +4.0¢ per $1
  - kalshi: Arizona State Senate winner? — 2 outcomes, +4.0¢ per $1
  - kalshi: Pro Baseball Championship Series MVP Winner — 23 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 10, settled: 0, still open: 10

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
