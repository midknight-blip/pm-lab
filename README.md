# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-28T01:17:47Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-28T00:36:12Z — 233 of 247 pairs priced
- Scans in the last 24h: 33 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-28T01:17:47Z — Kalshi 153073 markets, Polymarket 21403 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 529 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 219
- Positive pairs still in play: **329** (confirmed same bet: 3, not yet checked: 320)
- Scans with at least one positive pair: 528

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| KXCBDECISIONNZ-26OCT27-H25P /  | unsure | +98.0¢ | +68.9¢ | 369 | 50 | 0 | >999% |
| Highest temperature in San Francisco on Oct 2 / Will the highest temperature in San Francisco | no | +98.0¢ | +11.2¢ | 33 | 50 | 1 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| KXDFBPOKALSCORE-26OCT27BOCM05-BOC5M051 /  | no | +91.7¢ | +21.1¢ | 3 | 1 | 0 | >999% |
| Highest temperature in Atlanta on Oct 27, 202 / Will the highest temperature in Atlanta be be | no | +82.9¢ | +15.7¢ | 41 | 50 | 1 | >999% |
| Highest temperature in Atlanta on Oct 27, 202 / Will the highest temperature in Atlanta be be | no | +82.1¢ | +15.0¢ | 41 | 50 | 1 | >999% |
| KXCBDECISIONKOREA-26NOV25-H25P /  | no | +81.0¢ | +80.6¢ | 9 | 36 | 29 | >999% |
| Highest temperature in Chicago on Oct 27, 202 / Will the highest temperature in Chicago be be | no | +76.0¢ | +16.3¢ | 29 | 50 | 1 | >999% |

- Fast-check sessions (every 15 sec): 11 run, 175 positive spreads seen; typical one lasted 3660 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 369. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: College Basketball (M): #1 Ranked Team on Nov 9 AP Poll — 11 outcomes, +4.0¢ per $1
  - kalshi: Top AI model this month — 3 outcomes, +4.0¢ per $1
  - polymarket: Lowest temperature in Seoul (Incheon) on October 26? 15°C — 3 outcomes, +4.0¢ per $1
  - polymarket: New South Wales Parliamentary Election Winner Labor — 4 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Karachi on October 26? 38°C — 2 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 40, settled: 9, still open: 31
- Accuracy score (lower is better): Claude 0.209, market 0.176 → so far the market is more accurate; gap +0.033 (± 0.042). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 8 bets, $3.17 staked, result $-0.28 (-9%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
