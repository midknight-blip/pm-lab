# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-11-05T04:25:17Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-11-05T04:25:14Z — 246 of 249 pairs priced
- Scans in the last 24h: 24 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-11-05T01:26:02Z — Kalshi 178988 markets, Polymarket 21690 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 759 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 316
- Positive pairs still in play: **333** (confirmed same bet: 6, not yet checked: 311)
- Scans with at least one positive pair: 758

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXCBDECISIONNZ-26OCT27-H25P /  | unsure | +98.0¢ | +68.9¢ | 369 | 50 | 0 | >999% |
| KXBUNDESLIGASCORE-26OCT30SVEM05-SVE5M051 /  | unsure | +98.0¢ | +84.6¢ | 3 | 50 | 0 | >999% |
| KXAFCCLGAME-26NOV02WASQUW-WAS /  | no | +96.8¢ | +82.0¢ | 5 | 50 | 0 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXDFBPOKALSCORE-26OCT27BOCM05-BOC5M051 /  | unsure | +91.7¢ | +21.1¢ | 3 | 1 | 0 | >999% |
| KXAFCCLSCORE-26NOV03NUJSHP-NUJ0SHP1 /  | no | +87.4¢ | +42.8¢ | 8 | 50 | 0 | >999% |
| KXAFCCLGAME-26NOV02ITJAIN-ITJ /  | no | +81.2¢ | +6.7¢ | 18 | 50 | 0 | >999% |
| KXAFCCLGAME-26OCT26ALNWAS-ALN /  | unsure | +74.7¢ | +68.4¢ | 38 | 50 | 0 | >999% |
| Al Ahli Saudi vs Al-Taawoun Tie / Will Al Ahli Saudi Club vs. Al Taawoun Saudi  | no | +67.7¢ | +61.1¢ | 41 | 50 | 3 | >999% |

- Fast-check sessions (every 15 sec): 19 run, 243 positive spreads seen; typical one lasted 4770 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 237. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: US Sassuolo Calcio vs. ACF Fiorentina - Exact Score US Sassuolo Calcio — 14 outcomes, +4.0¢ per $1
  - kalshi: Who will be the next commissioner of Women's Pro Basketball? — 33 outcomes, +4.0¢ per $1
  - polymarket: October Inflation US - Monthly ≤0.1% — 4 outcomes, +4.0¢ per $1
  - polymarket: Senate Combo: Texas, Michigan, Maine Dems sweep — 4 outcomes, +4.0¢ per $1
  - polymarket: Next Premier of Victoria Jess Wilson — 3 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 60, settled: 29, still open: 35
- Accuracy score (lower is better): Claude 0.184, market 0.137 → so far the market is more accurate; gap +0.047 (± 0.024). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 22 bets, $8.55 staked, result $-1.84 (-22%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
