# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-24T01:08:21Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-24T00:30:28Z — 237 of 249 pairs priced
- Scans in the last 24h: 38 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-24T01:08:20Z — Kalshi 170038 markets, Polymarket 21586 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 378 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 156
- Positive pairs still in play: **274** (confirmed same bet: 0, not yet checked: 268)
- Scans with at least one positive pair: 377

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | unsure | +85.9¢ | +62.8¢ | 264 | 50 | 4 | >999% |
| KXHIGHTSEA-26OCT17-B60.5 /  | no | +51.7¢ | +6.2¢ | 16 | 46 | 1 | >999% |
| KXHIGHMIA-26OCT16-B88.5 /  | no | +48.2¢ | +25.6¢ | 37 | 50 | 1 | >999% |
| Highest temperature in Dallas on Oct 23, 2026 / Will the highest temperature in Dallas be bet | no | +45.6¢ | +22.4¢ | 12 | 50 | 1 | >999% |
| Highest temperature in Atlanta on Oct 23, 202 / Will the highest temperature in Atlanta be be | no | +43.2¢ | +22.3¢ | 20 | 50 | 1 | >999% |
| Highest temperature in Atlanta on Oct 23, 202 / Will the highest temperature in Atlanta be be | no | +41.3¢ | +10.3¢ | 19 | 50 | 1 | >999% |
| KXHIGHMIA-26OCT16-B90.5 /  | no | +40.9¢ | +22.8¢ | 38 | 50 | 1 | >999% |
| KXHIGHDEN-26OCT18-B76.5 /  | no | +40.8¢ | +8.5¢ | 16 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 8 run, 144 positive spreads seen; typical one lasted 2445 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 400. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: How many 6.5 or above earthquakes worldwide October 19 - October 25? 1 — 2 outcomes, +4.0¢ per $1
  - polymarket: Second-best Text Arena Math AI Lab end of October? Google — 2 outcomes, +4.0¢ per $1
  - polymarket: Niagara-on-the-Lake, ON Mayoral Election Winner Andrea Kaiser — 2 outcomes, +4.0¢ per $1
  - polymarket: How many House seats will the Democrats win in Minnesota? 4 — 2 outcomes, +4.0¢ per $1
  - polymarket: Pennsylvania State Senate Winner 2026? Democratic Party — 2 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 30, settled: 4, still open: 26
- Accuracy score (lower is better): Claude 0.128, market 0.122 → so far the market is more accurate; gap +0.006 (± 0.077). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 4 bets, $1.41 staked, result $+0.54 (+38%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
