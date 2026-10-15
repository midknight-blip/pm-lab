# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-15T11:31:48Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-15T11:31:45Z — 224 of 224 pairs priced
- Scans in the last 24h: 34 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-15T07:03:21Z — Kalshi 133295 markets, Polymarket 21143 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 34 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 76
- Positive pairs still in play: **40** (confirmed same bet: 0, not yet checked: 37)
- Scans with at least one positive pair: 34

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Midterms: which party wins white women? Repub / Will Republicans win white women in the midte | unsure | +7.0¢ | +3.8¢ | 32 | 50 | 24 | 111% |
| KXRANKLISTGOOGLESEARCHTOP5-26-LIN /  | unsure | +6.3¢ | +5.2¢ | 15 | 50 | 78 | 31% |
| Arizona State Senate winner? Republican party / Will the Republican Party control the Arizona | unsure | +5.4¢ | +2.4¢ | 6 | 20 | 20 | 103% |
| How low will the 30-year US Treasury yield ge / Will the 30-year Treasury yield dip below 5.5 | no | +3.7¢ | +1.7¢ | 14 | 27 | 17 | 83% |
| Israeli legislative election winner? Yashar / Will Yashar win the most seats in the 2026 Is | no | +3.4¢ | +2.1¢ | 13 | 50 | 13 | 102% |
| Highest temperature in Seattle on Oct 15, 202 / Will the highest temperature in Seattle be be | no | +3.1¢ | +2.2¢ | 5 | 10 | 1 | 882% |
| Top 5 most searched people on Google in 2026  / Will Nicolás Maduro rank in Google’s Top 5 Mo | no | +2.2¢ | +2.2¢ | 6 | 5 | 78 | 11% |
| Midterms: which party wins Latino men? Republ / Will Republicans win Latino men in the midter | no | +2.2¢ | +1.8¢ | 14 | 50 | 24 | 34% |
| Highest temperature in Miami on Oct 15, 2026? / Will the highest temperature in Miami be betw | no | +2.1¢ | +0.2¢ | 5 | 37 | 1 | 584% |
| Copa do Brasil Champion Palmeiras / Will Palmeiras win the 2026 Copa do Brasil? | no | +1.8¢ | +1.8¢ | 33 | 1 | 53 | 12% |

- Fast-check sessions (every 15 sec): 1 run, 10 positive spreads seen; typical one lasted 7200 sec, longest 120.0 min
- Same-site bundles in the last 3 days: 150. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Central Bank of Colombia decision in October 25 bps increase — 2 outcomes, +4.0¢ per $1
  - polymarket: Pro Football: 2026-27 Last Winless Team Los Angeles Chargers — 3 outcomes, +3.8¢ per $1
  - polymarket: Dancing with the Stars S35: Winner? Ezra Frech — 6 outcomes, +3.8¢ per $1
  - polymarket: Highest temperature in Chongqing on October 16? 28°C — 6 outcomes, +3.8¢ per $1
  - polymarket: Highest temperature in Austin on October 16? 70-71°F — 6 outcomes, +3.7¢ per $1

## Forecast test

No forecasts yet. First batch comes at the next Monday/Thursday check-in.

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
