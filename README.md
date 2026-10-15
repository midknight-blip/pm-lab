# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-15T00:25:05Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-15T00:25:02Z — 204 of 215 pairs priced
- Scans in the last 24h: 16 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-14T18:59:20Z — Kalshi 132892 markets, Polymarket 20699 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 16 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 71
- Positive pairs still in play: **25** (confirmed same bet: 0, not yet checked: 25)
- Scans with at least one positive pair: 16

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Midterms: which party wins white women? Repub / Will Republicans win white women in the midte | no | +7.0¢ | +4.4¢ | 14 | 50 | 25 | 111% |
| Top 5 most searched people on Google in 2026  / Will Lindsay Clancy rank in Google’s Top 5 Mo | no | +6.3¢ | +5.2¢ | 15 | 50 | 78 | 31% |
| Arizona State Senate winner? Republican party / Will the Republican Party control the Arizona | no | +5.4¢ | +5.4¢ | 3 | 20 | 20 | 103% |
| Top 5 most searched people on Google in 2026  / Will Bad Bunny rank in Google’s Top 5 Most Se | no | +4.1¢ | +2.1¢ | 2 | 13 | 78 | 20% |
| Israeli legislative election winner? Yashar / Will Yashar win the most seats in the 2026 Is | no | +2.4¢ | +2.4¢ | 5 | 50 | 13 | 67% |
| Top 5 most searched people on Google in 2026  / Will Nicolás Maduro rank in Google’s Top 5 Mo | no | +2.2¢ | +2.2¢ | 6 | 5 | 78 | 11% |
| Copa do Brasil Champion Palmeiras / Will Palmeiras win the 2026 Copa do Brasil? | no | +1.8¢ | +1.8¢ | 15 | 1 | 53 | 12% |
| Time's Person of the Year for 2026 Bernie San / Will Bernie Sanders be TIME Person of the Yea | no | +1.8¢ | +1.8¢ | 15 | 50 | 79 | 8% |
| Israeli legislative election winner? Likud / Will Likud win the most seats in the 2026 Isr | no | +1.4¢ | +0.4¢ | 8 | 50 | 13 | 38% |
| Time's Person of the Year for 2026 Marco Rubi / Will Marco Rubio be TIME Person of the Year 2 | no | +1.2¢ | +0.6¢ | 15 | 50 | 79 | 5% |

- Fast-check sessions (every 15 sec): none yet
- Same-site bundles in the last 3 days: 93. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Central Bank of Colombia decision in October 25 bps increase — 2 outcomes, +4.0¢ per $1
  - polymarket: Pro Football: 2026-27 Last Winless Team Los Angeles Chargers — 3 outcomes, +3.8¢ per $1
  - polymarket: Sokoto, Nigeria Governor Election Winner Ahmed Aliyu — 4 outcomes, +3.7¢ per $1
  - polymarket: IA-01 House Election Margin of Victory Republican 0-3% — 8 outcomes, +3.6¢ per $1
  - kalshi: Arizona State Senate winner? — 2 outcomes, +3.6¢ per $1

## Forecast test

No forecasts yet. First batch comes at the next Monday/Thursday check-in.

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
