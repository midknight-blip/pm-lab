# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-26T10:55:42Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-26T10:55:39Z — 223 of 223 pairs priced
- Scans in the last 24h: 40 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-26T07:08:26Z — Kalshi 138162 markets, Polymarket 22389 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 480 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 219
- Positive pairs still in play: **275** (confirmed same bet: 3, not yet checked: 266)
- Scans with at least one positive pair: 479

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | unsure | +94.8¢ | +68.9¢ | 320 | 50 | 2 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXHIGHTSEA-26OCT17-B60.5 /  | no | +51.7¢ | +6.2¢ | 16 | 46 | 1 | >999% |
| KXHIGHMIA-26OCT16-B88.5 /  | no | +48.2¢ | +25.6¢ | 37 | 50 | 1 | >999% |
| KXHIGHMIA-26OCT16-B90.5 /  | no | +40.9¢ | +22.8¢ | 38 | 50 | 1 | >999% |
| KXHIGHDEN-26OCT18-B76.5 /  | no | +40.8¢ | +8.5¢ | 16 | 50 | 1 | >999% |
| KXLIGAFGAME-26OCT17ATHVAL-ATH /  | no | +39.8¢ | +18.1¢ | 54 | 50 | 0 | >999% |
| KXHIGHMIA-26OCT18-B80.5 /  | no | +37.6¢ | +21.7¢ | 10 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 9 run, 150 positive spreads seen; typical one lasted 3023 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 356. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Highest temperature in Mexico City on October 24? 21°C — 3 outcomes, +4.0¢ per $1
  - polymarket: Who will receive the first mandate to form Israel's next government? G — 2 outcomes, +4.0¢ per $1
  - polymarket: SpaceX' Market Cap end of October 2026? $2.00-$2.25T — 4 outcomes, +4.0¢ per $1
  - polymarket: Second-best AI Lab end of October? Anthropic — 2 outcomes, +4.0¢ per $1
  - kalshi: College Basketball (M): #1 Ranked Team on Nov 9 AP Poll — 11 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 30, settled: 5, still open: 25
- Accuracy score (lower is better): Claude 0.169, market 0.147 → so far the market is more accurate; gap +0.023 (± 0.062). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 5 bets, $1.91 staked, result $+0.02 (+1%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
