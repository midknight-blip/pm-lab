# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-27T21:26:53Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-27T21:26:50Z — 245 of 247 pairs priced
- Scans in the last 24h: 33 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-27T19:00:14Z — Kalshi 148278 markets, Polymarket 21559 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 524 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 219
- Positive pairs still in play: **328** (confirmed same bet: 3, not yet checked: 319)
- Scans with at least one positive pair: 523

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXBELGIANPLGAME-26OCT24RAFCRCH-RAFC /  | no | +98.8¢ | +53.4¢ | 6 | 50 | 0 | >999% |
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | unsure | +98.0¢ | +68.9¢ | 364 | 50 | 0 | >999% |
| KXSAUDIPLGAME-26OCT19FAYAAS-FAY /  | unsure | +93.7¢ | +57.2¢ | 24 | 50 | 0 | >999% |
| VfL Bochum vs FSV Mainz: Correct Score VfL Bo / Will VfL Bochum win on 2026-10-27? | no | +91.7¢ | +21.1¢ | 3 | 1 | 0 | >999% |
| Highest temperature in Atlanta on Oct 27, 202 / Will the highest temperature in Atlanta be be | no | +82.9¢ | +15.7¢ | 41 | 50 | 1 | >999% |
| Highest temperature in Atlanta on Oct 27, 202 / Will the highest temperature in Atlanta be be | no | +82.1¢ | +15.0¢ | 41 | 50 | 1 | >999% |
| Bank of Korea rate decision in November Hike  / Will the Bank of Korea hike by 25 bps at the  | no | +79.0¢ | +77.8¢ | 4 | 36 | 29 | >999% |
| Highest temperature in Chicago on Oct 27, 202 / Will the highest temperature in Chicago be be | no | +76.0¢ | +16.5¢ | 25 | 50 | 1 | >999% |
| Highest temperature in Chicago on Oct 27, 202 / Will the highest temperature in Chicago be be | no | +75.0¢ | +38.1¢ | 28 | 34 | 1 | >999% |

- Fast-check sessions (every 15 sec): 11 run, 175 positive spreads seen; typical one lasted 3660 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 364. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: College Basketball (M): #1 Ranked Team on Nov 9 AP Poll — 11 outcomes, +4.0¢ per $1
  - kalshi: Top AI model this month — 3 outcomes, +4.0¢ per $1
  - polymarket: Lowest temperature in Seoul (Incheon) on October 26? 15°C — 3 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Karachi on October 26? 38°C — 2 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Jeddah on October 26? 36°C — 3 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 40, settled: 9, still open: 31
- Accuracy score (lower is better): Claude 0.209, market 0.176 → so far the market is more accurate; gap +0.033 (± 0.042). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 8 bets, $3.17 staked, result $-0.28 (-9%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
