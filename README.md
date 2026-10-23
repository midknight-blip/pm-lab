# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-23T03:16:15Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-23T03:16:12Z — 250 of 250 pairs priced
- Scans in the last 24h: 37 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 1
- Last market list refresh: 2026-10-23T01:06:41Z — Kalshi 165971 markets, Polymarket 22336 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 344 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 156
- Positive pairs still in play: **243** (confirmed same bet: 0, not yet checked: 237)
- Scans with at least one positive pair: 343

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXCBDECISIONNZ-26OCT27-H25P /  | unsure | +73.9¢ | +62.8¢ | 253 | 50 | 6 | >999% |
| KXHIGHTSEA-26OCT17-B60.5 /  | no | +51.7¢ | +6.2¢ | 16 | 46 | 1 | >999% |
| KXHIGHMIA-26OCT16-B88.5 /  | no | +48.2¢ | +25.6¢ | 37 | 50 | 1 | >999% |
| KXHIGHMIA-26OCT16-B90.5 /  | no | +40.9¢ | +22.8¢ | 38 | 50 | 1 | >999% |
| KXHIGHDEN-26OCT18-B76.5 /  | no | +40.8¢ | +8.5¢ | 16 | 50 | 1 | >999% |
| KXLIGAFGAME-26OCT17ATHVAL-ATH /  | no | +39.8¢ | +18.1¢ | 54 | 50 | 0 | >999% |
| KXHIGHMIA-26OCT18-B80.5 /  | no | +37.6¢ | +21.7¢ | 10 | 50 | 1 | >999% |
| KXHIGHTHOU-26OCT18-B72.5 /  | no | +32.1¢ | +16.0¢ | 16 | 33 | 1 | >999% |

- Fast-check sessions (every 15 sec): 7 run, 129 positive spreads seen; typical one lasted 2100 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 412. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Kansas Senate Election: Sedgwick County Winner Adam Hamilton (D) — 2 outcomes, +4.0¢ per $1
  - polymarket: Second-best Text Arena Math AI Lab end of October? Google — 2 outcomes, +4.0¢ per $1
  - polymarket: Keisha Lance Bottoms runs behind Jon Ossoff by...? (First Round) 3-6 p — 3 outcomes, +4.0¢ per $1
  - kalshi: Georgia State House winner? — 2 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Lucknow on October 22? 31°C — 2 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 30, settled: 4, still open: 26
- Accuracy score (lower is better): Claude 0.128, market 0.122 → so far the market is more accurate; gap +0.006 (± 0.077). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 4 bets, $1.41 staked, result $+0.54 (+38%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
