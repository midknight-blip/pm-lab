# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-15T14:18:17Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-15T14:18:13Z — 231 of 231 pairs priced
- Scans in the last 24h: 38 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-15T13:03:34Z — Kalshi 139232 markets, Polymarket 21824 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 38 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 76
- Positive pairs still in play: **43** (confirmed same bet: 0, not yet checked: 40)
- Scans with at least one positive pair: 38

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | no | +48.6¢ | +48.6¢ | 2 | 50 | 13 | >999% |
| Midterms: which party wins white women? Repub / Will Republicans win white women in the midte | unsure | +7.0¢ | +3.8¢ | 36 | 50 | 24 | 111% |
| KXRANKLISTGOOGLESEARCHTOP5-26-LIN /  | unsure | +6.3¢ | +5.2¢ | 15 | 50 | 78 | 31% |
| Arizona State Senate winner? Republican party / Will the Republican Party control the Arizona | unsure | +5.4¢ | +1.3¢ | 10 | 20 | 20 | 103% |
| Highest temperature in Miami on Oct 15, 2026? / Will the highest temperature in Miami be betw | no | +4.9¢ | +1.1¢ | 9 | 37 | 1 | >999% |
| How low will the 30-year US Treasury yield ge / Will the 30-year Treasury yield dip below 5.5 | no | +3.7¢ | +1.7¢ | 18 | 27 | 17 | 83% |
| Israeli legislative election winner? Yashar / Will Yashar win the most seats in the 2026 Is | no | +3.4¢ | +0.9¢ | 16 | 50 | 13 | 102% |
| Highest temperature in Seattle on Oct 15, 202 / Will the highest temperature in Seattle be be | no | +3.1¢ | +1.8¢ | 8 | 15 | 1 | 882% |
| Where will it rain on Oct 15, 2026? Washingto / Will it rain in Washington, DC on October 15? | no | +2.4¢ | +1.4¢ | 2 | 3 | 2 | 546% |
| Top 5 most searched people on Google in 2026  / Will Nicolás Maduro rank in Google’s Top 5 Mo | no | +2.2¢ | +2.2¢ | 6 | 5 | 78 | 11% |

- Fast-check sessions (every 15 sec): 1 run, 10 positive spreads seen; typical one lasted 7200 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 185. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: NM-03 House Election Margin of Victory Democrat 20-25% — 2 outcomes, +4.0¢ per $1
  - polymarket: Third-best AI Lab end of December? Alibaba — 18 outcomes, +4.0¢ per $1
  - polymarket: Central Bank of Colombia decision in October 25 bps increase — 2 outcomes, +4.0¢ per $1
  - polymarket: Borno, Nigeria Governor Election Winner Babagana Buhari — 3 outcomes, +4.0¢ per $1
  - polymarket: Pro Football: 2026-27 Last Winless Team Los Angeles Chargers — 3 outcomes, +3.8¢ per $1

## Forecast test

- Forecasts made: 10, settled: 0, still open: 10

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
