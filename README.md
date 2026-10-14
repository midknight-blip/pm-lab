# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-14T17:31:26Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-14T17:10:44Z — 76 of 76 pairs priced
- Scans in the last 24h: 1 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-14T17:31:26Z — Kalshi 133089 markets, Polymarket 21377 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 1 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Pairs that were ever positive: **40** (confirmed same bet: 0, not yet checked: 40)
- Scans with at least one positive pair: 1

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| KXVPRESPERSON-29-GNEW /  | no | +5.5¢ | +5.5¢ | 1 | 50 | 756 | 3% |
| KXPRESMATCHUP-28NOV07-AOCJVAN /  | no | +3.4¢ | +3.4¢ | 1 | 50 | 755 | 2% |
| KXVPRESPERSON-29-GWHI /  | no | +2.4¢ | +2.4¢ | 1 | 50 | 756 | 1% |
| KXPRESNOMD-28-AOC /  | no | +2.3¢ | +2.3¢ | 1 | 50 | 755 | 1% |
| KXVPRESPERSON-29-ESLO /  | no | +1.8¢ | +1.8¢ | 1 | 50 | 756 | 1% |
| KXVPRESPERSON-29-JOSS /  | no | +1.7¢ | +1.7¢ | 1 | 50 | 756 | 1% |
| KXPRESNOMD-28-BS /  | no | +1.6¢ | +1.6¢ | 1 | 50 | 755 | 1% |
| KXVPRESPERSON-29-JTAL /  | no | +1.4¢ | +1.4¢ | 1 | 50 | 756 | 1% |
| KXPRESNOMD-28-AB /  | no | +1.2¢ | +1.2¢ | 1 | 50 | 755 | 1% |
| KXPRESNOMD-28-MO /  | no | +1.2¢ | +1.2¢ | 1 | 23 | 755 | 1% |

- Fast-check sessions (every 15 sec): none yet
- Same-site bundles in the last 3 days: 158. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - kalshi: Iowa Republican Senate nominee in 2028? — 7 outcomes, +10.0¢ per $1
  - kalshi: Who will be Israeli justice minister after the election? — 15 outcomes, +10.0¢ per $1
  - kalshi: #2 Most Searched Person on Google in 2026? — 11 outcomes, +10.0¢ per $1
  - polymarket: What will OpenAI's IPO valuation be? $2.5T+ — 5 outcomes, +10.0¢ per $1
  - polymarket: SC Corinthians Paulista vs. EC Vitória SC Corinthians Paulista — 2 outcomes, +9.8¢ per $1

## Forecast test

No forecasts yet. First batch comes at the next Monday/Thursday check-in.

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
