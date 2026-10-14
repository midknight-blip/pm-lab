# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-14T17:10:47Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: never — 0 of 0 pairs priced
- Scans in the last 24h: 0 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-14T17:10:46Z — Kalshi 132708 markets, Polymarket 100 yes/no markets, 76 matched pairs

## Arbitrage test

Running since 2026-10-14. 1 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Pairs that were ever positive: **40** (confirmed same bet: 0, not yet checked: 40)
- Scans with at least one positive pair: 1

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| 2028 U.S. Vice-Presidential Election winner G / Will Gavin Newsom win the 2028 US Presidentia | no | +5.5¢ | +5.5¢ | 1 | 50 | 756 | 3% |
| 2028 Presidential matchup AOC v. JD Vance / Will JD Vance win the 2028 US Presidential El | no | +3.4¢ | +3.4¢ | 1 | 50 | 755 | 2% |
| 2028 U.S. Vice-Presidential Election winner G / Will Gretchen Whitmer win the 2028 US Preside | no | +2.4¢ | +2.4¢ | 1 | 50 | 756 | 1% |
| 2028 Democratic presidential nominee Alexandr / Will Alexandria Ocasio-Cortez win the 2028 De | no | +2.3¢ | +2.3¢ | 1 | 50 | 755 | 1% |
| 2028 U.S. Vice-Presidential Election winner E / Will Elissa Slotkin win the 2028 US President | no | +1.8¢ | +1.8¢ | 1 | 50 | 756 | 1% |
| 2028 U.S. Vice-Presidential Election winner J / Will Jon Ossoff win the 2028 US Presidential  | no | +1.7¢ | +1.7¢ | 1 | 50 | 756 | 1% |
| 2028 Democratic presidential nominee Bernie S / Will Bernie Sanders win the 2028 Democratic p | no | +1.6¢ | +1.6¢ | 1 | 50 | 755 | 1% |
| 2028 U.S. Vice-Presidential Election winner J / Will James Talarico win the 2028 US President | no | +1.4¢ | +1.4¢ | 1 | 50 | 756 | 1% |
| 2028 Democratic presidential nominee Andy Bes / Will Andy Beshear win the 2028 Democratic pre | no | +1.2¢ | +1.2¢ | 1 | 50 | 755 | 1% |
| 2028 Democratic presidential nominee Michelle / Will Michelle Obama win the 2028 Democratic p | no | +1.2¢ | +1.2¢ | 1 | 23 | 755 | 1% |

- Fast-check sessions (every 15 sec): none yet
- Same-site bundles in the last 3 days: 23. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: Iowa Republican Senate nominee in 2028? — 7 outcomes, +10.0¢ per $1
  - kalshi: Who will be Israeli justice minister after the election? — 15 outcomes, +10.0¢ per $1
  - kalshi: Alaska State House winner? — 2 outcomes, +8.0¢ per $1
  - kalshi: New Hampshire State Senate winner? — 2 outcomes, +7.0¢ per $1
  - polymarket: Presidential Election Winner 2028 JD Vance — 45 outcomes, +6.4¢ per $1

## Forecast test

No forecasts yet. First batch comes at the next Monday/Thursday check-in.

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
