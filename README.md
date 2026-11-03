# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-11-03T12:38:13Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-11-03T12:38:11Z — 243 of 246 pairs priced
- Scans in the last 24h: 26 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-11-03T07:30:53Z — Kalshi 151674 markets, Polymarket 23924 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 718 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 316
- Positive pairs still in play: **314** (confirmed same bet: 6, not yet checked: 292)
- Scans with at least one positive pair: 717

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXCBDECISIONNZ-26OCT27-H25P /  | unsure | +98.0¢ | +68.9¢ | 369 | 50 | 0 | >999% |
| KXBUNDESLIGASCORE-26OCT30SVEM05-SVE5M051 /  | unsure | +98.0¢ | +84.6¢ | 3 | 50 | 0 | >999% |
| KXAFCCLGAME-26NOV02WASQUW-WAS /  | no | +96.8¢ | +82.0¢ | 5 | 50 | 0 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXDFBPOKALSCORE-26OCT27BOCM05-BOC5M051 /  | unsure | +91.7¢ | +21.1¢ | 3 | 1 | 0 | >999% |
| Newcastle United Jets vs Shanghai Port FC: Co / Will Shanghai Port FC win on 2026-11-03? | no | +87.4¢ | +42.8¢ | 8 | 50 | 0 | >999% |
| KXAFCCLGAME-26NOV02ITJAIN-ITJ /  | no | +81.2¢ | +6.7¢ | 18 | 50 | 0 | >999% |
| KXAFCCLGAME-26OCT26ALNWAS-ALN /  | unsure | +74.7¢ | +68.4¢ | 38 | 50 | 0 | >999% |
| KXLIGUE1SCORE-26OCT30HACPSG-HAC0PSG1 /  | unsure | +67.6¢ | +66.1¢ | 14 | 50 | 0 | >999% |

- Fast-check sessions (every 15 sec): 17 run, 231 positive spreads seen; typical one lasted 3495 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 239. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Cross River, Nigeria Governor Election Winner Arthur Jarvis — 2 outcomes, +4.0¢ per $1
  - polymarket: Which party will win white women in the midterms? Republicans — 2 outcomes, +4.0¢ per $1
  - polymarket: How many more Millennium Prize Problems will AI solve in 2026? 0 — 2 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Guangzhou on November 1? 31°C — 3 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in London on November 2? 12°C — 2 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 60, settled: 23, still open: 40
- Accuracy score (lower is better): Claude 0.217, market 0.160 → so far the market is more accurate; gap +0.057 (± 0.030). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 20 bets, $7.52 staked, result $-1.79 (-24%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
