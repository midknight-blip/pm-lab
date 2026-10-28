# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-28T15:02:07Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-28T15:02:04Z — 250 of 250 pairs priced
- Scans in the last 24h: 31 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-28T13:18:32Z — Kalshi 153993 markets, Polymarket 21655 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 546 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 311
- Positive pairs still in play: **251** (confirmed same bet: 5, not yet checked: 240)
- Scans with at least one positive pair: 545

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXCBDECISIONNZ-26OCT27-H25P /  | unsure | +98.0¢ | +68.9¢ | 369 | 50 | 0 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXDFBPOKALSCORE-26OCT27BOCM05-BOC5M051 /  | no | +91.7¢ | +21.1¢ | 3 | 1 | 0 | >999% |
| Bank of Korea rate decision in November Hike  / Will the Bank of Korea hike by 25 bps at the  | no | +81.0¢ | +79.0¢ | 11 | 36 | 28 | >999% |
| KXAFCCLGAME-26OCT26ALNWAS-ALN /  | no | +74.7¢ | +68.4¢ | 38 | 50 | 0 | >999% |
| CMA Awards: Female Vocalist of the Year Ella  / Will Ella Langley win Female Vocalist of the  | no | +62.6¢ | +62.6¢ | 2 | 25 | 22 | >999% |
| KXDFBPOKALSCORE-26OCT27BOCM05-BOC1M055 /  | no | +55.6¢ | +54.6¢ | 5 | 50 | 0 | >999% |
| KXLIGAFGAME-26OCT17ATHVAL-ATH /  | no | +39.8¢ | +18.1¢ | 54 | 50 | 0 | >999% |
| KXISLGAME-26OCT251455HAJHTA-HTA /  | no | +30.3¢ | +30.3¢ | 4 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 11 run, 175 positive spreads seen; typical one lasted 3660 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 359. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: College Basketball (M): #1 Ranked Team on Nov 9 AP Poll — 11 outcomes, +4.0¢ per $1
  - kalshi: Top AI model this month — 3 outcomes, +4.0¢ per $1
  - polymarket: #2 Spotify Artist in October? Rihanna — 2 outcomes, +4.0¢ per $1
  - polymarket: Vermont Governor Election: Turnout 300K-325K — 3 outcomes, +4.0¢ per $1
  - polymarket: 3rd Largest Company end of October? Alphabet — 2 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 40, settled: 9, still open: 31
- Accuracy score (lower is better): Claude 0.209, market 0.176 → so far the market is more accurate; gap +0.033 (± 0.042). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 8 bets, $3.17 staked, result $-0.28 (-9%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
