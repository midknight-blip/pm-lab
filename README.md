# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-11-18T02:26:10Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-11-18T02:26:07Z — 215 of 248 pairs priced
- Scans in the last 24h: 4 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-11-17T21:01:05Z — Kalshi 164450 markets, Polymarket 21126 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 955 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 318
- Positive pairs still in play: **426** (confirmed same bet: 12, not yet checked: 374)
- Scans with at least one positive pair: 954

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXCBDECISIONNZ-26OCT27-H25P /  | unsure | +98.0¢ | +68.9¢ | 369 | 50 | 0 | >999% |
| KXBUNDESLIGASCORE-26OCT30SVEM05-SVE5M051 /  | unsure | +98.0¢ | +84.6¢ | 3 | 50 | 0 | >999% |
| KXEFLCHAMPIONSHIPGAME-26NOV07BRCNOR-BRC /  | unsure | +97.7¢ | +2.2¢ | 14 | 50 | 0 | >999% |
| KXAFCCLGAME-26NOV02WASQUW-WAS /  | unsure | +96.8¢ | +82.0¢ | 5 | 50 | 0 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXDFBPOKALSCORE-26OCT27BOCM05-BOC5M051 /  | unsure | +91.7¢ | +21.1¢ | 3 | 1 | 0 | >999% |
| KXAFCCLSCORE-26NOV03NUJSHP-NUJ0SHP1 /  | unsure | +87.4¢ | +42.8¢ | 8 | 50 | 0 | >999% |
| KXAFCCLGAME-26NOV02ITJAIN-ITJ /  | unsure | +81.2¢ | +6.7¢ | 18 | 50 | 0 | >999% |
| KXQSTARSGAME-26NOV08SADALR-SAD /  | unsure | +74.9¢ | +1.2¢ | 18 | 50 | 0 | >999% |

- Fast-check sessions (every 15 sec): 29 run, 487 positive spreads seen; typical one lasted 345 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 141. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: Grammy winner · Best Progressive R&B Album — 11 outcomes, +4.0¢ per $1
  - kalshi: Big Sky Men's Conference Tournament Champion — 11 outcomes, +4.0¢ per $1
  - polymarket: Oyo, Nigeria Governor Election Winner Yusuf Akim Adebola — 7 outcomes, +4.0¢ per $1
  - polymarket: Spain General Election: Burgos Winner PP — 5 outcomes, +4.0¢ per $1
  - polymarket: Oscars 2027: Best Animated Short Film Winner Dog Alone — 11 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 90, settled: 65, still open: 26
- Accuracy score (lower is better): Claude 0.180, market 0.124 → so far the market is more accurate; gap +0.057 (± 0.020). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 51 bets, $17.99 staked, result $-2.64 (-15%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
