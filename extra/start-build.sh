#!/usr/bin/env bash
#
# start-build.sh — simulate a slow external job for the Lab 10 /goal demo.
#
# Launches a detached background "build" that writes its progress to a status
# file over real wall-clock time, then finishes with "BUILD COMPLETE". Because
# the job runs on its own schedule, a /goal loop that polls the status file
# genuinely spans several turns — the agent can't make it finish any faster.
#
# Usage:
#   bash extra/start-build.sh                 # ~60s job, writes ./build-status.txt
#   STATUS_FILE=foo.txt STEPS=8 SECS=5 bash extra/start-build.sh
#
STATUS_FILE="${STATUS_FILE:-build-status.txt}"
STEPS="${STEPS:-5}"        # number of progress steps before completion
SECS="${SECS:-8}"          # seconds per step (5 x 8 = ~40s total)

# Detach so the job keeps running after this script returns and the terminal is free.
nohup bash -c '
  status="'"$STATUS_FILE"'"; steps='"$STEPS"'; secs='"$SECS"'
  for i in $(seq 1 "$steps"); do
    echo "BUILDING — step $i/$steps" > "$status"
    sleep "$secs"
  done
  echo "BUILD COMPLETE" > "$status"
' >/dev/null 2>&1 &

echo "BUILDING — step 0/$STEPS" > "$STATUS_FILE"
echo "Started a background build -> $STATUS_FILE (~$((STEPS * SECS))s, $STEPS steps)."
echo "It will progress step by step, then write 'BUILD COMPLETE'. Nothing can speed it up."