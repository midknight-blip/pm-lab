# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-26T15:00:27Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-26T14:04:21Z — 223 of 223 pairs priced
- Scans in the last 24h: 34 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-26T15:00:26Z — Kalshi 142016 markets, Polymarket 22147 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 482 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 219
- Positive pairs still in play: **275** (confirmed same bet: 3, not yet checked: 266)
- Scans with at least one positive pair: 481

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | unsure | +94.8¢ | +68.9¢ | 322 | 50 | 2 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXHIGHTSEA-26OCT17-B60.5 /  | no | +51.7¢ | +6.2¢ | 16 | 46 | 1 | >999% |
| KXHIGHMIA-26OCT16-B88.5 /  | no | +48.2¢ | +25.6¢ | 37 | 50 | 1 | >999% |
| KXHIGHMIA-26OCT16-B90.5 /  | no | +40.9¢ | +22.8¢ | 38 | 50 | 1 | >999% |
| KXHIGHDEN-26OCT18-B76.5 /  | no | +40.8¢ | +8.5¢ | 16 | 50 | 1 | >999% |
| KXLIGAFGAME-26OCT17ATHVAL-ATH /  | no | +39.8¢ | +18.1¢ | 54 | 50 | 0 | >999% |
| KXHIGHMIA-26OCT18-B80.5 /  | no | +37.6¢ | +21.7¢ | 10 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 9 run, 150 positive spreads seen; typical one lasted 3023 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 348. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: College Basketball (M): #1 Ranked Team on Nov 9 AP Poll — 11 outcomes, +4.0¢ per $1
  - polymarket: How many 6.5 or above earthquakes worldwide October 19 - October 25? 1 — 2 outcomes, +4.0¢ per $1
  - polymarket: Who will receive the first mandate to form Israel's next government? G — 2 outcomes, +4.0¢ per $1
  - polymarket: #2 Spotify Artist in October? Rihanna — 2 outcomes, +4.0¢ per $1
  - polymarket: AZ-02 House Election Margin of Victory Republican 6-9% — 3 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 40, settled: 9, still open: 33
- Accuracy score (lower is better): Claude 0.209, market 0.176 → so far the market is more accurate; gap +0.033 (± 0.042). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 8 bets, $3.17 staked, result $-0.28 (-9%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
