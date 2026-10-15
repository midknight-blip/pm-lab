# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-15T19:26:20Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-15T19:26:17Z — 230 of 230 pairs priced
- Scans in the last 24h: 40 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-15T18:58:14Z — Kalshi 142988 markets, Polymarket 20919 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 46 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 76
- Positive pairs still in play: **63** (confirmed same bet: 0, not yet checked: 60)
- Scans with at least one positive pair: 46

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | no | +48.6¢ | +48.6¢ | 10 | 50 | 12 | >999% |
| Highest temperature in Miami on Oct 16, 2026? / Will the highest temperature in Miami be betw | no | +21.2¢ | +21.2¢ | 1 | 10 | 2 | >999% |
| Highest temperature in Dallas on Oct 16, 2026 / Will the highest temperature in Dallas be bet | no | +20.8¢ | +20.8¢ | 1 | 50 | 2 | >999% |
| Highest temperature in San Francisco on Oct 1 / Will the highest temperature in San Francisco | no | +19.8¢ | +19.8¢ | 1 | 5 | 2 | >999% |
| Highest temperature in Miami on Oct 16, 2026? / Will the highest temperature in Miami be betw | no | +17.2¢ | +17.2¢ | 1 | 8 | 2 | >999% |
| Highest temperature in San Francisco on Oct 1 / Will the highest temperature in San Francisco | no | +7.8¢ | +7.8¢ | 1 | 18 | 2 | >999% |
| Midterms: which party wins white women? Repub / Will Republicans win white women in the midte | unsure | +7.0¢ | +2.9¢ | 44 | 50 | 24 | 111% |
| KXRANKLISTGOOGLESEARCHTOP5-26-LIN /  | unsure | +6.3¢ | +5.2¢ | 15 | 50 | 78 | 31% |
| How low will the 10-year US Treasury yield ge / Will the 10-year Treasury yield dip below 5.0 | no | +5.8¢ | +5.8¢ | 1 | 0 | 16 | 136% |
| Highest temperature in Dallas on Oct 16, 2026 / Will the highest temperature in Dallas be bet | no | +5.5¢ | +5.5¢ | 1 | 50 | 2 | >999% |

- Fast-check sessions (every 15 sec): 1 run, 10 positive spreads seen; typical one lasted 7200 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 221. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: NM-03 House Election Margin of Victory Democrat 20-25% — 2 outcomes, +4.0¢ per $1
  - polymarket: Third-best AI Lab end of December? Alibaba — 18 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Shanghai on October 17? 28°C — 3 outcomes, +4.0¢ per $1
  - polymarket: Central Bank of Colombia decision in October 25 bps increase — 2 outcomes, +4.0¢ per $1
  - polymarket: Borno, Nigeria Governor Election Winner Babagana Buhari — 3 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 10, settled: 0, still open: 10

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
