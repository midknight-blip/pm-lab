# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-16T10:00:39Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-16T10:00:36Z — 241 of 242 pairs priced
- Scans in the last 24h: 40 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-16T07:02:43Z — Kalshi 139015 markets, Polymarket 20808 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 71 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 76
- Positive pairs still in play: **83** (confirmed same bet: 0, not yet checked: 80)
- Scans with at least one positive pair: 71

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | no | +49.7¢ | +48.6¢ | 35 | 50 | 12 | >999% |
| Highest temperature in Miami on Oct 16, 2026? / Will the highest temperature in Miami be betw | no | +36.4¢ | +22.2¢ | 26 | 50 | 1 | >999% |
| Highest temperature in Miami on Oct 16, 2026? / Will the highest temperature in Miami be betw | no | +32.4¢ | +13.9¢ | 26 | 50 | 1 | >999% |
| Highest temperature in Dallas on Oct 16, 2026 / Will the highest temperature in Dallas be bet | no | +27.8¢ | +11.8¢ | 24 | 50 | 1 | >999% |
| Highest temperature in Dallas on Oct 16, 2026 / Will the highest temperature in Dallas be bet | no | +23.6¢ | +16.4¢ | 20 | 50 | 1 | >999% |
| Highest temperature in San Francisco on Oct 1 / Will the highest temperature in San Francisco | no | +22.0¢ | +10.8¢ | 26 | 50 | 1 | >999% |
| Athletic vs Valencia Athletic / Will Athletic Club win on 2026-10-17? | no | +18.2¢ | +13.0¢ | 2 | 50 | 1 | >999% |
| Highest temperature in San Francisco on Oct 1 / Will the highest temperature in San Francisco | no | +13.6¢ | +8.4¢ | 26 | 50 | 1 | >999% |
| Highest temperature in San Francisco on Oct 1 / Will the highest temperature in San Francisco | no | +12.5¢ | +5.2¢ | 20 | 50 | 1 | >999% |
| Highest temperature in Chicago on Oct 16, 202 / Will the highest temperature in Chicago be be | no | +12.3¢ | +1.9¢ | 16 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 1 run, 10 positive spreads seen; typical one lasted 7200 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 272. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: Detroit: Stage of Elimination — 6 outcomes, +4.0¢ per $1
  - polymarket: NM-03 House Election Margin of Victory Democrat 20-25% — 2 outcomes, +4.0¢ per $1
  - polymarket: Third-best AI Lab end of December? Alibaba — 18 outcomes, +4.0¢ per $1
  - polymarket: Who will be UFC Lightweight champion at the end of 2026? Justin Gaethj — 2 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Shanghai on October 17? 28°C — 3 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 10, settled: 0, still open: 10

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
