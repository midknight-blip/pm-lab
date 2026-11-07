# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-11-07T01:10:00Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-11-07T01:09:58Z — 242 of 247 pairs priced
- Scans in the last 24h: 26 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-11-06T19:10:49Z — Kalshi 183941 markets, Polymarket 22082 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 805 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 316
- Positive pairs still in play: **349** (confirmed same bet: 7, not yet checked: 319)
- Scans with at least one positive pair: 804

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXCBDECISIONNZ-26OCT27-H25P /  | unsure | +98.0¢ | +68.9¢ | 369 | 50 | 0 | >999% |
| KXBUNDESLIGASCORE-26OCT30SVEM05-SVE5M051 /  | unsure | +98.0¢ | +84.6¢ | 3 | 50 | 0 | >999% |
| KXAFCCLGAME-26NOV02WASQUW-WAS /  | unsure | +96.8¢ | +82.0¢ | 5 | 50 | 0 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXDFBPOKALSCORE-26OCT27BOCM05-BOC5M051 /  | unsure | +91.7¢ | +21.1¢ | 3 | 1 | 0 | >999% |
| KXAFCCLSCORE-26NOV03NUJSHP-NUJ0SHP1 /  | unsure | +87.4¢ | +42.8¢ | 8 | 50 | 0 | >999% |
| KXAFCCLGAME-26NOV02ITJAIN-ITJ /  | unsure | +81.2¢ | +6.7¢ | 18 | 50 | 0 | >999% |
| KXAFCCLGAME-26OCT26ALNWAS-ALN /  | unsure | +74.7¢ | +68.4¢ | 38 | 50 | 0 | >999% |
| Al Ahli Saudi vs Al-Taawoun Tie / Will Al Ahli Saudi Club vs. Al Taawoun Saudi  | same | +69.3¢ | +66.8¢ | 87 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 20 run, 247 positive spreads seen; typical one lasted 4785 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 220. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: AFCON 2027 Qualifying: Group I Winner Burundi — 4 outcomes, +4.0¢ per $1
  - kalshi: Who will be the next commissioner of Women's Pro Basketball? — 33 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Austin on November 6? 76-77°F — 3 outcomes, +4.0¢ per $1
  - kalshi: 120th Congress: Who will be Senate Minority Leader? — 8 outcomes, +4.0¢ per $1
  - polymarket: Which company has the best Text-to-Image AI end of December? OpenAI — 2 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 70, settled: 32, still open: 39
- Accuracy score (lower is better): Claude 0.183, market 0.126 → so far the market is more accurate; gap +0.057 (± 0.024). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 25 bets, $9.01 staked, result $-2.31 (-26%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
