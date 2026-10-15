# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-15T18:58:14Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-15T18:52:25Z — 231 of 231 pairs priced
- Scans in the last 24h: 40 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-15T18:58:14Z — Kalshi 142988 markets, Polymarket 20919 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 45 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 76
- Positive pairs still in play: **51** (confirmed same bet: 0, not yet checked: 48)
- Scans with at least one positive pair: 45

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Reserve Bank of New Zealand rate decision in  / Reserve Bank of New Zealand increases interes | no | +48.6¢ | +48.6¢ | 9 | 50 | 12 | >999% |
| Midterms: which party wins white women? Repub / Will Republicans win white women in the midte | unsure | +7.0¢ | +2.9¢ | 43 | 50 | 24 | 111% |
| KXRANKLISTGOOGLESEARCHTOP5-26-LIN /  | unsure | +6.3¢ | +5.2¢ | 15 | 50 | 78 | 31% |
| How low will the 10-year US Treasury yield ge / Will the 10-year Treasury yield dip below 5.0 | no | +5.8¢ | +5.8¢ | 1 | 0 | 16 | 136% |
| KXSTATELEG-AZSEN26-R /  | unsure | +5.4¢ | +1.3¢ | 10 | 20 | 20 | 103% |
| Highest temperature in Miami on Oct 15, 2026? / Will the highest temperature in Miami be betw | no | +4.9¢ | +1.3¢ | 12 | 41 | 1 | >999% |
| How low will the 30-year US Treasury yield ge / Will the 30-year Treasury yield dip below 5.5 | no | +3.7¢ | +1.7¢ | 24 | 50 | 16 | 83% |
| Israeli legislative election winner? Yashar / Will Yashar win the most seats in the 2026 Is | no | +3.4¢ | +0.4¢ | 23 | 50 | 12 | 102% |
| Highest temperature in Seattle on Oct 15, 202 / Will the highest temperature in Seattle be be | no | +3.1¢ | +1.8¢ | 8 | 15 | 1 | 882% |
| Minnesota State Senate winner? Democratic par / Will the Democratic Party control the Minneso | no | +2.5¢ | +2.5¢ | 4 | 50 | 19 | 48% |

- Fast-check sessions (every 15 sec): 1 run, 10 positive spreads seen; typical one lasted 7200 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 221. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: NM-03 House Election Margin of Victory Democrat 20-25% — 2 outcomes, +4.0¢ per $1
  - polymarket: Third-best AI Lab end of December? Alibaba — 18 outcomes, +4.0¢ per $1
  - polymarket: Highest temperature in Shanghai on October 17? 28°C — 3 outcomes, +4.0¢ per $1
  - polymarket: Central Bank of Colombia decision in October 25 bps increase — 2 outcomes, +4.0¢ per $1
  - polymarket: Borno, Nigeria Governor Election Winner Babagana Buhari — 3 outcomes, +4.0¢ per $1

## Forecast test

- Forecasts made: 10, settled: 0, still open: 10

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
