# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-22T02:24:31Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-22T02:24:27Z — 248 of 248 pairs priced
- Scans in the last 24h: 37 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-22T01:03:05Z — Kalshi 162017 markets, Polymarket 22018 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 306 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 84
- Positive pairs still in play: **284** (confirmed same bet: 0, not yet checked: 281)
- Scans with at least one positive pair: 306

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Highest temperature in Denver on Oct 21, 2026 / Will the highest temperature in Denver be bet | no | +98.8¢ | +8.7¢ | 30 | 50 | 1 | >999% |
| Highest temperature in Denver on Oct 21, 2026 / Will the highest temperature in Denver be bet | no | +98.8¢ | +9.4¢ | 37 | 50 | 1 | >999% |
| KXHIGHTSEA-26OCT18-B60.5 /  | no | +98.8¢ | +72.8¢ | 29 | 50 | 0 | >999% |
| KXHIGHTHOU-26OCT19-B78.5 /  | no | +98.8¢ | +16.8¢ | 55 | 50 | 1 | >999% |
| KXHIGHTHOU-26OCT19-B80.5 /  | no | +98.8¢ | +16.2¢ | 57 | 50 | 1 | >999% |
| KXHIGHTATL-26OCT19-B70.5 /  | no | +98.8¢ | +17.2¢ | 51 | 50 | 1 | >999% |
| KXHIGHTATL-26OCT19-B68.5 /  | no | +98.8¢ | +18.4¢ | 45 | 50 | 1 | >999% |
| KXHIGHDEN-26OCT20-B72.5 /  | no | +98.7¢ | +9.2¢ | 36 | 50 | 1 | >999% |
| KXHIGHTSFO-26OCT17-B82.5 /  | no | +98.3¢ | +4.5¢ | 16 | 50 | 1 | >999% |
| KXHIGHTSFO-26OCT20-B68.5 /  | no | +98.2¢ | +12.3¢ | 54 | 50 | 0 | >999% |

- Fast-check sessions (every 15 sec): 6 run, 117 positive spreads seen; typical one lasted 1785 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 386. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Niagara-on-the-Lake, ON Mayoral Election Winner Andrea Kaiser — 2 outcomes, +4.0¢ per $1
  - polymarket: Kansas Senate Election: Sedgwick County Winner Adam Hamilton (D) — 2 outcomes, +4.0¢ per $1
  - polymarket: Second-best Text Arena Math AI Lab end of October? Google — 2 outcomes, +4.0¢ per $1
  - polymarket: Keisha Lance Bottoms runs behind Jon Ossoff by...? (First Round) 3-6 p — 3 outcomes, +4.0¢ per $1
  - kalshi: Georgia State House winner? — 2 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 20, settled: 4, still open: 16
- Accuracy score (lower is better): Claude 0.128, market 0.122 → so far the market is more accurate; gap +0.006 (± 0.077). Needs ~100 settled before this means much.
- Paper bets (when Claude disagreed by 5+ points): 4 bets, $1.41 staked, result $+0.54 (+38%)

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
