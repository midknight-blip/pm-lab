# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-15T08:26:21Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-15T08:26:19Z — 229 of 229 pairs priced
- Scans in the last 24h: 29 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-15T07:03:21Z — Kalshi 133295 markets, Polymarket 21143 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 29 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 71
- Positive pairs still in play: **40** (confirmed same bet: 0, not yet checked: 40)
- Scans with at least one positive pair: 29

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Midterms: which party wins white women? Repub / Will Republicans win white women in the midte | no | +7.0¢ | +3.9¢ | 27 | 50 | 24 | 111% |
| KXRANKLISTGOOGLESEARCHTOP5-26-LIN /  | no | +6.3¢ | +5.2¢ | 15 | 50 | 78 | 31% |
| How low will the 2-year US Treasury yield get / Will the 2-year Treasury yield dip below 4.73 | no | +5.7¢ | +5.7¢ | 1 | 50 | 17 | 131% |
| Arizona State Senate winner? Republican party / Will the Republican Party control the Arizona | no | +5.4¢ | +5.4¢ | 3 | 20 | 20 | 103% |
| How low will the 5-year US Treasury yield get / Will the 5-year Treasury yield dip below 4.95 | no | +4.5¢ | +4.5¢ | 5 | 0 | 17 | 103% |
| Top 5 most searched people on Google in 2026  / Will Bad Bunny rank in Google’s Top 5 Most Se | no | +4.1¢ | +4.1¢ | 14 | 13 | 78 | 20% |
| Leeds United vs Manchester United Leeds Unite / Will Manchester United FC win on 2026-10-18? | no | +3.2¢ | +3.2¢ | 2 | 50 | 3 | 366% |
| Highest temperature in Dallas on Oct 15, 2026 / Will the highest temperature in Dallas be bet | no | +2.7¢ | +2.7¢ | 2 | 1 | 1 | 701% |
| Israeli legislative election winner? Yashar / Will Yashar win the most seats in the 2026 Is | no | +2.4¢ | +0.4¢ | 9 | 50 | 13 | 67% |
| Top 5 most searched people on Google in 2026  / Will Nicolás Maduro rank in Google’s Top 5 Mo | no | +2.2¢ | +2.2¢ | 6 | 5 | 78 | 11% |

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
