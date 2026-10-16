# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-16T03:43:53Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-16T03:43:51Z — 233 of 233 pairs priced
- Scans in the last 24h: 40 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-16T00:58:13Z — Kalshi 145547 markets, Polymarket 21248 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 61 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 76
- Positive pairs still in play: **78** (confirmed same bet: 0, not yet checked: 75)
- Scans with at least one positive pair: 61

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | no | +49.7¢ | +48.6¢ | 25 | 50 | 12 | >999% |
| Highest temperature in Miami on Oct 16, 2026? / Will the highest temperature in Miami be betw | no | +32.6¢ | +20.1¢ | 16 | 50 | 2 | >999% |
| Highest temperature in Miami on Oct 16, 2026? / Will the highest temperature in Miami be betw | no | +26.2¢ | +12.3¢ | 16 | 50 | 2 | >999% |
| Highest temperature in Dallas on Oct 16, 2026 / Will the highest temperature in Dallas be bet | no | +23.6¢ | +19.9¢ | 16 | 50 | 2 | >999% |
| Highest temperature in Dallas on Oct 16, 2026 / Will the highest temperature in Dallas be bet | no | +22.0¢ | +12.4¢ | 16 | 50 | 2 | >999% |
| Highest temperature in San Francisco on Oct 1 / Will the highest temperature in San Francisco | no | +22.0¢ | +15.8¢ | 16 | 50 | 2 | >999% |
| Athletic vs Valencia Athletic / Will Athletic Club win on 2026-10-17? | no | +18.2¢ | +18.2¢ | 1 | 50 | 2 | >999% |
| Highest temperature in San Francisco on Oct 1 / Will the highest temperature in San Francisco | no | +13.4¢ | +9.2¢ | 16 | 20 | 2 | >999% |
| Highest temperature in Miami on Oct 16, 2026? / Will the highest temperature in Miami be betw | no | +10.0¢ | +5.3¢ | 16 | 50 | 2 | >999% |
| Highest temperature in San Francisco on Oct 1 / Will the highest temperature in San Francisco | no | +9.3¢ | +4.2¢ | 12 | 50 | 2 | >999% |

- Fast-check sessions (every 15 sec): 1 run, 10 positive spreads seen; typical one lasted 7200 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 248. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: NM-03 House Election Margin of Victory Democrat 20-25% — 2 outcomes, +4.0¢ per $1
  - polymarket: Third-best AI Lab end of December? Alibaba — 18 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Shanghai on October 17? 28°C — 3 outcomes, +4.0¢ per $1
  - polymarket: Central Bank of Colombia decision in October 25 bps increase — 2 outcomes, +4.0¢ per $1
  - polymarket: Borno, Nigeria Governor Election Winner Babagana Buhari — 3 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 10, settled: 0, still open: 10

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
