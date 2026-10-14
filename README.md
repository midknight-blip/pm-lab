# pm-lab

Read-only test of two ideas on Kalshi and Polymarket. No money is involved. Updated automatically — last update 2026-10-14T18:14:58Z.

1. **Arbitrage:** do the two sites ever price the same event so that buying both sides locks in a profit after fees?
2. **Forecasting:** can Claude's researched probabilities beat the market price?

## Health

- Last scan: 2026-10-14T18:14:55Z — 215 of 215 pairs priced
- Scans in the last 24h: 5 (GitHub runs these roughly every 15 min; 60-96 is normal), errors: 0
- Last market list refresh: 2026-10-14T17:52:35Z — Kalshi 133154 markets, Polymarket 21300 yes/no markets, 250 matched pairs

## Arbitrage test

Running since 2026-10-14. 5 scans so far. A pair counts as positive when buying both sides costs less than $1 after fees, at the best available price.

- Positive pairs ruled out as different bets after reading the rules: 71
- Positive pairs still in play: **15** (confirmed same bet: 0, not yet checked: 15)
- Scans with at least one positive pair: 5

| Pair (Kalshi / Polymarket) | Checked | Best | Median | Times seen | Max size | Days left | Best yearly |
|---|---|---|---|---|---|---|---|
| Top 5 most searched people on Google in 2026  / Will Lindsay Clancy rank in Google’s Top 5 Mo | no | +6.3¢ | +6.3¢ | 4 | 50 | 78 | 31% |
| Top 5 most searched people on Google in 2026  / Will Nicolás Maduro rank in Google’s Top 5 Mo | no | +2.2¢ | +2.2¢ | 3 | 5 | 78 | 11% |
| Copa do Brasil Champion Palmeiras / Will Palmeiras win the 2026 Copa do Brasil? | no | +1.8¢ | +1.8¢ | 4 | 1 | 53 | 12% |
| Time's Person of the Year for 2026 Bernie San / Will Bernie Sanders be TIME Person of the Yea | no | +1.8¢ | +1.8¢ | 4 | 50 | 79 | 8% |
| Midterms: which party wins white women? Repub / Will Republicans win white women in the midte | no | +1.3¢ | +0.8¢ | 4 | 50 | 25 | 20% |
| Time's Person of the Year for 2026 Marco Rubi / Will Marco Rubio be TIME Person of the Year 2 | no | +1.2¢ | +1.2¢ | 4 | 40 | 79 | 5% |
| Texas State Senate winner? Republican party / Will the Republican Party control the Texas S | no | +1.1¢ | +1.1¢ | 4 | 50 | 20 | 20% |
| MotoGP World Champion Marco Bezzecchi / Will Marco Bezzecchi win the 2026 MotoGP Worl | no | +1.1¢ | +1.1¢ | 4 | 2 | 47 | 9% |
| Time's Person of the Year for 2026 James Tala / Will James Talarico be TIME Person of the Yea | no | +0.9¢ | +0.9¢ | 4 | 20 | 79 | 4% |
| CMA Awards: Vocal Group of the Year The Red C / Will The Red Clay Strays win Vocal Group of t | no | +0.7¢ | +0.7¢ | 1 | 4 | 35 | 8% |

- Fast-check sessions (every 15 sec): none yet
- Same-site bundles in the last 3 days: 78. These only work if the listed outcomes cover every possibility, which still needs checking. Top ones:
  - polymarket: Sokoto, Nigeria Governor Election Winner Ahmed Aliyu — 4 outcomes, +3.7¢ per $1
  - polymarket: IA-01 House Election Margin of Victory Republican 0-3% — 8 outcomes, +3.6¢ per $1
  - kalshi: Arizona State Senate winner? — 2 outcomes, +3.6¢ per $1
  - polymarket: Al-Taawoun FC vs. Al Rayyan SC Al-Taawoun FC — 2 outcomes, +3.5¢ per $1
  - polymarket: #3 Spotify Artist 2026 Taylor Swift — 2 outcomes, +3.3¢ per $1

## Forecast test

No forecasts yet. First batch comes at the next Monday/Thursday check-in.

---
How it works: `src/` has the code, `arb/` and `forecast/` hold the data. See `CHECKIN.md` for what the twice-weekly Claude check-in does.
