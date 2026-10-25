# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-25T11:40:45Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-25T11:40:42Z — 235 of 247 pairs priced
- Scans in the last 24h: 46 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-25T07:00:53Z — Kalshi 149671 markets, Polymarket 22245 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 442 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 156
- Positive pairs still in play: **311** (confirmed same bet: 0, not yet checked: 305)
- Scans with at least one positive pair: 441

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXHIGHMIA-26OCT24-B84.5 /  | no | +98.8¢ | +14.4¢ | 53 | 50 | 1 | >999% |
| KXHIGHTDAL-26OCT24-B84.5 /  | no | +98.8¢ | +13.3¢ | 60 | 50 | 1 | >999% |
| KXHIGHTDAL-26OCT24-B82.5 /  | no | +98.8¢ | +14.9¢ | 64 | 50 | 1 | >999% |
| KXHIGHMIA-26OCT24-B82.5 /  | no | +98.8¢ | +16.7¢ | 48 | 50 | 1 | >999% |
| Highest temperature in San Francisco on Oct 2 / Will the highest temperature in San Francisco | no | +98.8¢ | +98.8¢ | 21 | 50 | 0 | >999% |
| Highest temperature in San Francisco on Oct 2 / Will the highest temperature in San Francisco | no | +98.8¢ | +98.8¢ | 12 | 50 | 0 | >999% |
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXCBDECISIONNZ-26OCT27-H25P /  | unsure | +89.9¢ | +66.8¢ | 296 | 50 | 3 | >999% |

- Fast-check sessions (every 15 sec): 9 run, 150 positive spreads seen; typical one lasted 3023 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 360. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Highest temperature in Wellington on October 23? 20°C — 4 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Dallas on October 23? 82-83°F — 2 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Karachi on October 23? 36°C — 3 outcomes, +4.0¢ per $1
  - polymarket: Eurozone GDP growth in Q3 2026 1.2-1.5% — 2 outcomes, +4.0¢ per $1
  - polymarket: Khamenei # posts October 23 - October 30, 2026? <5 — 4 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 30, settled: 4, still open: 26
- Accuracy score (lower is better): Claude 0.128, market 0.122 → so far the market is more accurate; gap +0.006 (± 0.077). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 4 bets, $1.41 staked, result $+0.54 (+38%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
