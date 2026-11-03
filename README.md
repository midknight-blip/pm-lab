# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-11-03T02:13:21Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-11-03T02:13:18Z — 245 of 245 pairs priced
- Scans in the last 24h: 25 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-11-03T01:24:25Z — Kalshi 171586 markets, Polymarket 22383 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 707 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 316
- Positive pairs still in play: **312** (confirmed same bet: 6, not yet checked: 290)
- Scans with at least one positive pair: 706

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXCBDECISIONNZ-26OCT27-H25P /  | unsure | +98.0¢ | +68.9¢ | 369 | 50 | 0 | >999% |
| KXBUNDESLIGASCORE-26OCT30SVEM05-SVE5M051 /  | unsure | +98.0¢ | +84.6¢ | 3 | 50 | 0 | >999% |
| KXAFCCLGAME-26NOV02WASQUW-WAS /  | no | +96.8¢ | +82.0¢ | 5 | 50 | 0 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXDFBPOKALSCORE-26OCT27BOCM05-BOC5M051 /  | unsure | +91.7¢ | +21.1¢ | 3 | 1 | 0 | >999% |
| KXAFCCLGAME-26NOV02ITJAIN-ITJ /  | no | +81.2¢ | +6.7¢ | 18 | 50 | 0 | >999% |
| KXAFCCLGAME-26OCT26ALNWAS-ALN /  | unsure | +74.7¢ | +68.4¢ | 38 | 50 | 0 | >999% |
| KXLIGUE1SCORE-26OCT30HACPSG-HAC0PSG1 /  | unsure | +67.6¢ | +66.1¢ | 14 | 50 | 0 | >999% |
| Radnicki Nis vs FK Zeleznicar Pancevo Tie / Will FK Radnicki Nis vs. FK Zeleznicar Pancev | no | +65.7¢ | +56.4¢ | 9 | 50 | 0 | >999% |

- Fast-check sessions (every 15 sec): 16 run, 225 positive spreads seen; typical one lasted 3060 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 247. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Steam Weekly #1 Seller (October 27 - November 3) Call of Duty: Modern  — 2 outcomes, +4.0¢ per $1
  - polymarket: Which party will hold more governorships after the midterms? Democrati — 2 outcomes, +4.0¢ per $1
  - polymarket: Cross River, Nigeria Governor Election Winner Arthur Jarvis — 2 outcomes, +4.0¢ per $1
  - polymarket: Oscars 2027: Best Animated Feature Film Winner Toy Story 5 — 8 outcomes, +4.0¢ per $1
  - polymarket: Which party will win white women in the midterms? Republicans — 2 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 60, settled: 18, still open: 42
- Accuracy score (lower is better): Claude 0.204, market 0.168 → so far the market is more accurate; gap +0.036 (± 0.033). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 15 bets, $5.35 staked, result $-0.55 (-10%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
