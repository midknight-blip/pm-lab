# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-25T00:58:41Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-25T00:21:44Z — 243 of 247 pairs priced
- Scans in the last 24h: 44 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-25T00:58:40Z — Kalshi 157978 markets, Polymarket 22104 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 422 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 156
- Positive pairs still in play: **299** (confirmed same bet: 0, not yet checked: 293)
- Scans with at least one positive pair: 421

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Highest temperature in Miami on Oct 24, 2026? / Will the highest temperature in Miami be betw | no | +98.8¢ | +10.9¢ | 46 | 50 | 1 | >999% |
| Highest temperature in Dallas on Oct 24, 2026 / Will the highest temperature in Dallas be bet | no | +98.8¢ | +11.6¢ | 51 | 50 | 1 | >999% |
| Highest temperature in Dallas on Oct 24, 2026 / Will the highest temperature in Dallas be bet | no | +98.8¢ | +13.0¢ | 55 | 50 | 1 | >999% |
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| Highest temperature in Miami on Oct 24, 2026? / Will the highest temperature in Miami be betw | no | +98.4¢ | +13.5¢ | 41 | 50 | 1 | >999% |
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXCBDECISIONNZ-26OCT27-H25P /  | unsure | +89.9¢ | +66.8¢ | 296 | 50 | 3 | >999% |
| KXHIGHTSEA-26OCT17-B60.5 /  | no | +51.7¢ | +6.2¢ | 16 | 46 | 1 | >999% |
| KXHIGHMIA-26OCT16-B88.5 /  | no | +48.2¢ | +25.6¢ | 37 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 9 run, 150 positive spreads seen; typical one lasted 3023 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 386. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Visa (V) Q4 payments volume growth (constant dollars)? 9.5% to 10.5% — 4 outcomes, +4.0¢ per $1
  - polymarket: Niagara-on-the-Lake, ON Mayoral Election Winner Andrea Kaiser — 2 outcomes, +4.0¢ per $1
  - polymarket: Apple’s Market Cap end of 2026? $5.00-$5.50T — 3 outcomes, +4.0¢ per $1
  - polymarket: #1 Searched Actor on Google 2026? Jacob Elordi — 30 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Helsinki on October 23? 12°C — 2 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 30, settled: 4, still open: 26
- Accuracy score (lower is better): Claude 0.128, market 0.122 → so far the market is more accurate; gap +0.006 (± 0.077). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 4 bets, $1.41 staked, result $+0.54 (+38%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
