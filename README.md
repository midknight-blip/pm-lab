# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-31T14:45:01Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-31T14:44:59Z — 248 of 248 pairs priced
- Scans in the last 24h: 32 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-31T13:04:22Z — Kalshi 179532 markets, Polymarket 22331 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 634 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 313
- Positive pairs still in play: **286** (confirmed same bet: 6, not yet checked: 269)
- Scans with at least one positive pair: 633

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXCBDECISIONNZ-26OCT27-H25P /  | unsure | +98.0¢ | +68.9¢ | 369 | 50 | 0 | >999% |
| KXBUNDESLIGASCORE-26OCT30SVEM05-SVE5M051 /  | no | +98.0¢ | +84.6¢ | 3 | 50 | 0 | >999% |
| KXCBDECISIONENGLAND-26NOV05-H25P /  | no | +96.8¢ | +96.7¢ | 14 | 50 | 6 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXDFBPOKALSCORE-26OCT27BOCM05-BOC5M051 /  | unsure | +91.7¢ | +21.1¢ | 3 | 1 | 0 | >999% |
| KXAFCCLGAME-26OCT26ALNWAS-ALN /  | unsure | +74.7¢ | +68.4¢ | 38 | 50 | 0 | >999% |
| KXLIGUE1SCORE-26OCT30HACPSG-HAC0PSG1 /  | no | +67.6¢ | +66.1¢ | 14 | 50 | 0 | >999% |
| KXCMA-FVOTY26-ELAN /  | unsure | +62.6¢ | +62.0¢ | 6 | 30 | 21 | >999% |
| KXDFBPOKALSCORE-26OCT27BOCM05-BOC1M055 /  | unsure | +55.6¢ | +54.6¢ | 5 | 50 | 0 | >999% |

- Fast-check sessions (every 15 sec): 15 run, 213 positive spreads seen; typical one lasted 3316 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 325. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Highest temperature in Jeddah on October 29? 34°C — 3 outcomes, +4.0¢ per $1
  - polymarket: Bulgaria Presidential Election Second Round: Turnout 24%+ — 2 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Miami on October 30? 84-85°F — 2 outcomes, +4.0¢ per $1
  - polymarket: Pingtung County Magistrate Election Winner Su Ching-chuan — 2 outcomes, +4.0¢ per $1
  - polymarket: Iran leader end of 2026? Mojtaba Khamenei — 11 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 50, settled: 12, still open: 38
- Accuracy score (lower is better): Claude 0.225, market 0.158 → so far the market is more accurate; gap +0.068 (± 0.039). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 10 bets, $3.83 staked, result $-0.97 (-25%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
