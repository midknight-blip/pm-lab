#!/usr/bin/env bash
# Commit whatever the job changed and push, retrying if another job pushed first.
set -e
MSG="$1"
git config user.name "pm-lab-bot"
git config user.email "pm-lab-bot@users.noreply.github.com"
git add -A
if git diff --cached --quiet; then echo "nothing to commit"; exit 0; fi
git commit -qm "$MSG"
for i in 1 2 3 4 5 6; do
  if git pull -q --rebase -X theirs && git push -q; then exit 0; fi
  sleep $((i * 5))
done
echo "push failed"; exit 1
