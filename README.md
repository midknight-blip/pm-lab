# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-25T22:38:37Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-25T22:38:34Z — 240 of 247 pairs priced
- Scans in the last 24h: 45 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-25T18:53:33Z — Kalshi 149039 markets, Polymarket 22176 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 463 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 156
- Positive pairs still in play: **325** (confirmed same bet: 0, not yet checked: 319)
- Scans with at least one positive pair: 462

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXHIGHMIA-26OCT24-B84.5 /  | no | +98.8¢ | +14.4¢ | 53 | 50 | 1 | >999% |
| KXHIGHTDAL-26OCT24-B84.5 /  | no | +98.8¢ | +13.3¢ | 60 | 50 | 1 | >999% |
| KXHIGHTDAL-26OCT24-B82.5 /  | no | +98.8¢ | +14.9¢ | 64 | 50 | 1 | >999% |
| KXHIGHMIA-26OCT24-B82.5 /  | no | +98.8¢ | +16.7¢ | 48 | 50 | 1 | >999% |
| KXHIGHTSFO-26OCT24-B72.5 /  | no | +98.8¢ | +98.8¢ | 21 | 50 | 0 | >999% |
| KXHIGHTSFO-26OCT24-B74.5 /  | no | +98.8¢ | +98.8¢ | 12 | 50 | 0 | >999% |
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| Highest temperature in Chicago on Oct 25, 202 / Will the highest temperature in Chicago be be | no | +98.4¢ | +6.6¢ | 37 | 50 | 1 | >999% |
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| Highest temperature in Chicago on Oct 25, 202 / Will the highest temperature in Chicago be be | no | +98.0¢ | +6.2¢ | 41 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 9 run, 150 positive spreads seen; typical one lasted 3023 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 347. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Highest temperature in Austin on October 24? 88-89°F — 2 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Cape Town on October 24? 22°C — 3 outcomes, +4.0¢ per $1
  - polymarket: October Unemployment Rate 4.1% — 3 outcomes, +4.0¢ per $1
  - polymarket: Central Bank of Colombia decision in October No change — 2 outcomes, +4.0¢ per $1
  - polymarket: CZ # posts October 23 - October 30, 2026? 20-39 — 2 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 30, settled: 5, still open: 25
- Accuracy score (lower is better): Claude 0.169, market 0.147 → so far the market is more accurate; gap +0.023 (± 0.062). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 5 bets, $1.91 staked, result $+0.02 (+1%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
