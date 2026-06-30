#!/usr/bin/env bash
# Create the Lab 12 "ultrareview" demo branch + PR in skillrepos/cc-se.
# Run this from your cc-se checkout (this folder has origin -> skillrepos/cc-se).
# Requires: push access to the repo and an authenticated `gh` CLI (gh auth status).
set -euo pipefail

BRANCH="review-demo"
FILE="review-demo/user-store.js"
BODY="review-demo/PR-BODY.md"

# Confirm the demo file exists (created for you alongside this script).
test -f "$FILE" || { echo "Missing $FILE — run from the repo root."; exit 1; }

# Make sure we branch from an up-to-date main (adjust if your default differs).
git fetch origin
git checkout main
git pull --ff-only origin main

# Create the branch and commit ONLY the demo file (not PR-BODY.md).
git checkout -b "$BRANCH"
git add "$FILE"
git commit -m "Add review-demo/user-store.js (Lab 12 ultrareview fixture)"
git push -u origin "$BRANCH"

# Open the PR against main, keeping it open for the course.
gh pr create --base main --head "$BRANCH" \
  --title "Review demo: add a user store helper" \
  --body-file "$BODY"

echo
echo "PR created. Note its number — that's the <PR#> students pass to:"
echo "    claude ultrareview <PR#>"
