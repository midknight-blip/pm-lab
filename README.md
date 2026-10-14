# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-14T17:48:41Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-14T17:48:37Z — 250 of 250 pairs priced
- Scans in the last 24h: 3 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-14T17:48:10Z — Kalshi 133183 markets, Polymarket 21304 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 3 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Pairs that were ever positive: **85** (confirmed same bet: 0, not yet checked: 85)
- Scans with at least one positive pair: 3

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXHIGHMIA-26OCT15-B86.5 /  | no | +73.7¢ | +73.7¢ | 1 | 10 | 2 | 49905% |
| Highest temperature in Miami on Oct 14, 2026? / Will the highest temperature in Miami be betw | no | +70.4¢ | +70.4¢ | 1 | 5 | 1 | 82703% |
| Highest temperature in Miami on Oct 14, 2026? / Will the highest temperature in Miami be betw | no | +69.4¢ | +69.4¢ | 1 | 6 | 1 | 78776% |
| Highest temperature in Denver on Oct 14, 2026 / Will the highest temperature in Denver be bet | no | +61.3¢ | +59.6¢ | 2 | 50 | 1 | 54803% |
| Highest temperature in Denver on Oct 14, 2026 / Will the highest temperature in Denver be bet | no | +57.3¢ | +56.8¢ | 2 | 5 | 1 | 46558% |
| What will General Motors say during their nex / Will General Motors say "President" or "Trump | no | +56.1¢ | +56.1¢ | 2 | 50 | 6 | 7270% |
| KXHIGHMIA-26OCT15-B90.5 /  | no | +50.7¢ | +50.7¢ | 1 | 31 | 2 | 18289% |
| KXHIGHTDAL-26OCT15-B92.5 /  | no | +28.7¢ | +28.7¢ | 1 | 18 | 2 | 7156% |
| Highest temperature in Miami on Oct 15, 2026? / Will the highest temperature in Miami be betw | no | +21.2¢ | +21.2¢ | 1 | 26 | 2 | 4792% |
| KXHIGHMIA-26OCT15-B88.5 /  | no | +19.5¢ | +19.5¢ | 1 | 5 | 2 | 4315% |

- Fast-check sessions (every 15 sec): none yet
- Same-site bundles in the last 3 days: 187. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: Iowa Republican Senate nominee in 2028? — 7 outcomes, +10.0¢ per $1
  - kalshi: Who will be Israeli justice minister after the election? — 15 outcomes, +10.0¢ per $1
  - kalshi: #2 Most Searched Person on Google in 2026? — 11 outcomes, +10.0¢ per $1
  - polymarket: Copa Sudamericana 2026 Winner Boca Juniors — 3 outcomes, +10.0¢ per $1
  - polymarket: Republican House seats after the 2026 midterm elections? 190-194 — 7 outcomes, +10.0¢ per $1

## Forecast test

No forecasts yet. First batch comes at the next Monday/Thursday check-in.

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
