# Twice-weekly check-in (Monday and Thursday)

This is what the scheduled Claude session does. Keep it cheap: read the summary,
not the raw logs, unless one specific pair needs a closer look.

## 0. Get the latest
`git pull` in the pm-lab folder. Then read `README.md` and `arb/health.json`. Don't read `src/`.

## 1. Is the scanner healthy?
Flag it if any of these are true:
- last scan is more than 2 hours old
- fewer than 40 scans in the last 24h
- pairs priced is far below pairs watched, or matched pairs dropped sharply
- an error is showing
If GitHub Actions has stopped, say so plainly. The user can't see it otherwise.

## 2. Check new arbitrage pairs
Run `python tools/unreviewed.py 8`. For each pair, compare the two rules and decide:
- `same`: both settle on the same event, same threshold, same date and same source, so one wins exactly when the other loses
- `different`: they could settle differently (different date, threshold, source, "by" vs "on", how ties or overtime count, and so on)
- `unsure`: can't tell from the text

Record each one in `arb/pairs_review.json` as
`{"<pair_id>": {"status": "same|different|unsure", "note": "one line why", "checked": "YYYY-MM-DD"}}`
(add to the existing file, don't replace it). `different` pairs drop out of the scan.

Things worth calling out to the user:
- a big edge on a tiny size (e.g. 6¢ on $3)
- the same pair positive every day, which usually means a rules difference
- spreads that only show up right before settlement or overnight, which points to stale prices
- what the fast-check sessions say about how long spreads last

## 3. Forecast the new batch
Open the newest `forecast/queue/*.json` whose markets aren't in `forecast/forecasts.csv` yet.
For each market:
- Read the question and the rules carefully. The rules decide the answer, not the headline.
- Research with web search: news, official data, schedules, base rates. Aim for 1-3 searches per market.
- **Don't look up the price** on Kalshi, Polymarket, betting or odds sites. If a search result shows it anyway, set `saw_market_price: true`.
- Give a probability from 0.01 to 0.99, and a one-line reason.

Save the batch to a temp file and run `python tools/add_forecasts.py <file>`.
(Format is at the top of that script.)

## 4. Save
`git add -A && git commit -m "check-in YYYY-MM-DD" && git push`
The push triggers a GitHub job that records the market price at that moment, for the fair comparison.

## 5. Send the update
Send one short message in plain English (no jargon, no hype):
1. One-line headline: what the data says so far.
2. Arbitrage: what changed since last time, any pairs confirmed or rejected and why, anything odd.
3. Forecasts: how many done, the 2-3 where you disagreed most with what you'd guess the market thinks (you don't know the price yet), and the running score once forecasts have settled.
4. Scanner health, one line.
5. Anything the user should do, or "nothing needed".
Be honest when the result is "nothing interesting yet". Mark confidence as [Certain] / [Likely] / [Guessing].
