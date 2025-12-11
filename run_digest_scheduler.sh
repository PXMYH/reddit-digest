#!/usr/bin/env bash
set -euo pipefail

# Reddit Digest Scheduler
# Runs all 5 subreddit digests with rolling 7-day window
# Designed to be run via cron every 4 hours

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXECUTABLE="$SCRIPT_DIR/dist/reddit-digest"
DIGEST_DIR="$SCRIPT_DIR/digest"
LOG_DIR="$SCRIPT_DIR/logs"
LOG_FILE="$LOG_DIR/digest_$(date +%Y-%m-%d).log"

# Subreddits to process
SUBREDDITS=(
    "formula1"
    "LocalLLaMA"
    "Fire"
    "financialindependence"
    "Bogleheads"
)

# Filter thresholds
MIN_UPVOTES=100
MIN_COMMENTS=20

# Logging function
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Error handling
handle_error() {
    log "❌ Error on line $1"
    log "   Command: $BASH_COMMAND"
}

trap 'handle_error $LINENO' ERR

# Start
log "=========================================="
log "🤖 Reddit Digest Scheduler Started"
log "=========================================="

# Check if executable exists
if [ ! -f "$EXECUTABLE" ]; then
    log "❌ Error: Executable not found at $EXECUTABLE"
    log "   Run ./build_executable.sh first"
    exit 1
fi

# Create directories
mkdir -p "$DIGEST_DIR"
mkdir -p "$LOG_DIR"

# Calculate rolling 7-day date range
END_DATE=$(date +%Y-%m-%d)
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    START_DATE=$(date -v-7d +%Y-%m-%d)
else
    # Linux
    START_DATE=$(date -d '7 days ago' +%Y-%m-%d)
fi

log "📅 Date range: $START_DATE to $END_DATE"
log ""

# Process each subreddit
SUCCESS_COUNT=0
FAIL_COUNT=0

for subreddit in "${SUBREDDITS[@]}"; do
    log "📥 Processing r/$subreddit..."

    if "$EXECUTABLE" "$subreddit" \
        --start "$START_DATE" \
        --end "$END_DATE" \
        --min-upvotes "$MIN_UPVOTES" \
        --min-comments "$MIN_COMMENTS" \
        >> "$LOG_FILE" 2>&1; then

        log "   ✅ r/$subreddit completed successfully"
        ((SUCCESS_COUNT++))
    else
        log "   ❌ r/$subreddit failed (exit code: $?)"
        ((FAIL_COUNT++))
    fi

    log ""
done

# Git commit and push
log "📝 Committing results to git..."

cd "$SCRIPT_DIR"

if git add digest/ 2>> "$LOG_FILE"; then
    if git diff --staged --quiet; then
        log "   ℹ️  No changes to commit"
    else
        COMMIT_MSG="chore: update Reddit digests ($(date +'%Y-%m-%d %H:%M UTC'))"
        if git commit -m "$COMMIT_MSG" 2>> "$LOG_FILE" && \
           git push 2>> "$LOG_FILE"; then
            log "   ✅ Changes committed and pushed"
        else
            log "   ❌ Git push failed"
            FAIL_COUNT=$((FAIL_COUNT + 1))
        fi
    fi
else
    log "   ❌ Git add failed"
    FAIL_COUNT=$((FAIL_COUNT + 1))
fi

# Summary
log ""
log "=========================================="
log "📊 Summary"
log "=========================================="
log "✅ Successful: $SUCCESS_COUNT subreddits"
log "❌ Failed: $FAIL_COUNT subreddits"
log "📋 Log file: $LOG_FILE"
log ""

# Exit with error if any failures
if [ $FAIL_COUNT -gt 0 ]; then
    log "⚠️  Completed with $FAIL_COUNT error(s)"
    exit 1
else
    log "✨ All tasks completed successfully"
    exit 0
fi
