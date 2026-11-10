# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-11-10T00:44:31Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-11-10T00:44:29Z — 247 of 250 pairs priced
- Scans in the last 24h: 24 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-11-09T19:12:39Z — Kalshi 156187 markets, Polymarket 21530 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 890 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 316
- Positive pairs still in play: **372** (confirmed same bet: 10, not yet checked: 334)
- Scans with at least one positive pair: 889

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

- Fast-check sessions (every 15 sec): 22 run, 274 positive spreads seen; typical one lasted 4252 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 211. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: Who will be Ranking Member of House Judiciary? — 3 outcomes, +4.0¢ per $1
  - polymarket: How many different countries will the US conduct military action again — 2 outcomes, +4.0¢ per $1
  - polymarket: AFCON 2027 Qualifying: Group I Winner Burundi — 4 outcomes, +4.0¢ per $1
  - polymarket: Zelenskyy # posts November 3 - November 10, 2026? 100-119 — 2 outcomes, +4.0¢ per $1
  - polymarket: Which company's AI will first hit 1550 on Chatbot Arena in 2026? xAI — 3 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 80, settled: 40, still open: 42
- Accuracy score (lower is better): Claude 0.186, market 0.111 → so far the market is more accurate; gap +0.075 (± 0.022). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 31 bets, $10.43 staked, result $-3.80 (-36%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
