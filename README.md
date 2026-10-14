# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-14T17:44:23Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-14T17:44:21Z — 250 of 250 pairs priced
- Scans in the last 24h: 2 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-14T17:35:24Z — Kalshi 133123 markets, Polymarket 21374 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 2 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Pairs that were ever positive: **75** (confirmed same bet: 0, not yet checked: 75)
- Scans with at least one positive pair: 2

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Highest temperature in Miami on Oct 15, 2026? / Will the highest temperature in Miami be betw | no | +73.7¢ | +73.7¢ | 1 | 10 | 2 | 49905% |
| Highest temperature in Denver on Oct 14, 2026 / Will the highest temperature in Denver be bet | no | +61.3¢ | +61.3¢ | 1 | 6 | 1 | 54803% |
| Highest temperature in Denver on Oct 14, 2026 / Will the highest temperature in Denver be bet | no | +57.3¢ | +57.3¢ | 1 | 5 | 1 | 46558% |
| What will General Motors say during their nex / Will General Motors say "President" or "Trump | no | +56.1¢ | +56.1¢ | 1 | 50 | 6 | 7266% |
| Highest temperature in Miami on Oct 15, 2026? / Will the highest temperature in Miami be betw | no | +50.7¢ | +50.7¢ | 1 | 31 | 2 | 18289% |
| Highest temperature in Dallas on Oct 15, 2026 / Will the highest temperature in Dallas be bet | no | +28.7¢ | +28.7¢ | 1 | 18 | 2 | 7156% |
| Highest temperature in Miami on Oct 15, 2026? / Will the highest temperature in Miami be betw | no | +19.5¢ | +19.5¢ | 1 | 5 | 2 | 4315% |
| Swiss National Bank rate decision in December / Will the Swiss National Bank increase the SNB | no | +18.4¢ | +18.4¢ | 1 | 50 | 57 | 145% |
| Highest temperature in San Francisco on Oct 1 / Will the highest temperature in San Francisco | no | +9.8¢ | +9.8¢ | 1 | 26 | 2 | 1941% |
| Highest temperature in Seattle on Oct 15, 202 / Will the highest temperature in Seattle be be | no | +9.3¢ | +9.3¢ | 1 | 10 | 2 | 1821% |

- Fast-check sessions (every 15 sec): none yet
- Same-site bundles in the last 3 days: 168. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: Iowa Republican Senate nominee in 2028? — 7 outcomes, +10.0¢ per $1
  - kalshi: Who will be Israeli justice minister after the election? — 15 outcomes, +10.0¢ per $1
  - kalshi: #2 Most Searched Person on Google in 2026? — 11 outcomes, +10.0¢ per $1
  - polymarket: Copa Sudamericana 2026 Winner Boca Juniors — 3 outcomes, +10.0¢ per $1
  - polymarket: Republican House seats after the 2026 midterm elections? 190-194 — 7 outcomes, +10.0¢ per $1

## Forecast test

No forecasts yet. First batch comes at the next Monday/Thursday check-in.

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
