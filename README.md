# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-30T03:42:53Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-30T03:42:50Z — 245 of 245 pairs priced
- Scans in the last 24h: 28 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-30T01:19:06Z — Kalshi 165239 markets, Polymarket 22237 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 590 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 313
- Positive pairs still in play: **275** (confirmed same bet: 6, not yet checked: 258)
- Scans with at least one positive pair: 589

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXCBDECISIONNZ-26OCT27-H25P /  | unsure | +98.0¢ | +68.9¢ | 369 | 50 | 0 | >999% |
| Bank of England rate decision in November Hik / Bank of England increases interest rates by 2 | no | +96.7¢ | +96.6¢ | 3 | 50 | 7 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXDFBPOKALSCORE-26OCT27BOCM05-BOC5M051 /  | unsure | +91.7¢ | +21.1¢ | 3 | 1 | 0 | >999% |
| KXAFCCLGAME-26OCT26ALNWAS-ALN /  | unsure | +74.7¢ | +68.4¢ | 38 | 50 | 0 | >999% |
| Le Havre AC vs Paris Saint-Germain: Correct S / Will Paris Saint-Germain FC win on 2026-10-30 | no | +67.6¢ | +67.6¢ | 3 | 50 | 1 | >999% |
| CMA Awards: Female Vocalist of the Year Ella  / Will Ella Langley win Female Vocalist of the  | unsure | +62.6¢ | +62.0¢ | 6 | 30 | 21 | >999% |
| KXDFBPOKALSCORE-26OCT27BOCM05-BOC1M055 /  | unsure | +55.6¢ | +54.6¢ | 5 | 50 | 0 | >999% |
| Bank of Israel rate decision in November Cut  / Will the Bank of Israel decrease the Bank of  | no | +42.6¢ | +1.7¢ | 3 | 21 | 25 | >999% |

- Fast-check sessions (every 15 sec): 13 run, 197 positive spreads seen; typical one lasted 3420 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 377. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Central Bank of Colombia decision in October No change — 2 outcomes, +4.0¢ per $1
  - polymarket: Lowest temperature in Paris on October 28? 5°C — 3 outcomes, +4.0¢ per $1
  - polymarket: 3rd Largest Company end of October? Alphabet — 2 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Kuala Lumpur on October 28? 33°C — 4 outcomes, +4.0¢ per $1
  - polymarket: Senate Combo: Texas, Kansas, Nebraska Dems TX & KS, Ind NE — 4 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 50, settled: 11, still open: 40
- Accuracy score (lower is better): Claude 0.227, market 0.167 → so far the market is more accurate; gap +0.060 (± 0.042). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 9 bets, $3.59 staked, result $-0.72 (-20%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
