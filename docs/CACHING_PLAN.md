# Plan: Add Summary Caching to Reddit Digest

## Goal
Avoid re-summarizing posts that were already processed in previous runs by caching summaries keyed by `post_id`.

## Design Decisions
- **Cache storage**: Simple JSON file per subreddit (`cache/{subreddit}.json`)
- **Cache key**: `post_id` (Reddit's unique post identifier)
- **Invalidation**: Never - once summarized, always reuse
- **Default enabled**: Cache is ON by default, use `--no-cache` to disable

## Files to Modify

### 1. NEW: `reddit_summarizer/cache.py`
Simple cache class:
```python
class SummaryCache:
    def __init__(self, cache_dir="cache")
    def load(self, subreddit) -> None
    def get(self, subreddit, post_id) -> PostSummary | None
    def put(self, subreddit, post_id, summary: PostSummary) -> None
    def save(self, subreddit) -> None
    def get_stats(self, subreddit) -> dict
```

Cache file format (`cache/{subreddit}.json`):
```json
{
  "post_id_1": {"summary": "...", "key_points": [...], "discussion_highlights": "..."},
  "post_id_2": {...}
}
```

### 2. MODIFY: `reddit_summarizer/summarizer.py`
**Add cache:**
- Add `cache: SummaryCache = None` parameter to `__init__`
- In `generate_digest()` loop, before calling `summarize_post()`:
  - Check cache: `cached = self.cache.get(subreddit, post.post_id)`
  - If hit: use cached summary, increment counter
  - If miss: call LLM, then `self.cache.put()`
- After loop: `self.cache.save(subreddit)`
- Print cache stats (hits/misses)

**Remove checkpoint system:**
- Delete `_load_checkpoint()` method
- Delete `_save_checkpoint()` method
- Delete `_delete_checkpoint()` method
- Remove checkpoint parameters from `generate_digest()`
- Remove checkpoint logic (load at start, save in loop, delete on success)

### 3. MODIFY: `summarize_subreddit.py`
**Add cache options:**
```python
@click.option("--cache/--no-cache", default=True, help="Cache summaries to avoid re-processing (default: enabled)")
@click.option("--cache-dir", default="cache", help="Cache directory path")
```

**Remove checkpoint options:**
```python
# DELETE these lines:
@click.option("--checkpoint", ...)
@click.option("--checkpoint-interval", ...)
```

Initialize cache by default, skip if `--no-cache` is passed.

### 4. MODIFY: `reddit_summarizer/__init__.py`
Add `SummaryCache` to exports.

### 5. MODIFY: `.gitignore`
Add `cache/` directory.

### 6. NEW: `tests/test_cache.py`
Test cache hit/miss, save/load, corrupted file handling.

### 7. MODIFY: Documentation
**`CLAUDE.md`:**
- Remove `--checkpoint` and `--checkpoint-interval` from CLI examples
- Add `--cache` and `--cache-dir` options
- Update architecture section

**`docs/QUICK_START.md`:**
- Remove "Tip 2: Use Checkpoints for Large Jobs" section
- Update Quick Reference Card (remove checkpoint line)

**`docs/TECHNICAL.md`:**
- Remove checkpoint options from CLI table
- Add cache options to CLI table
- Remove "Checkpoint Support" section

## Edge Cases & Behavior

### Cache + Fast Mode (no `--summarize`)
- Cache is **only used when `--summarize` is enabled**
- Fast mode skips LLM entirely, so cache has no effect
- No cache file is created/updated in fast mode

### Cache + Date Range Mode
- Works the same as timeframe mode
- Cache is keyed by `post_id`, so posts overlapping between date ranges share cached summaries

### GitHub Actions Workflow
- Cache directory should be committed to repo for cross-run persistence
- OR: Use GitHub Actions cache to persist `cache/` directory between runs
- Decision: Keep `cache/` in `.gitignore` for local use, GHA can handle its own caching

### Error Handling
- **Corrupted cache file**: Log warning, treat as empty cache, continue without crashing
- **Permission errors**: Log warning, disable cache for this run, continue
- **Missing cache dir**: Create it automatically

### Cache File Locking
- Not needed for single-process CLI tool
- If running multiple instances in parallel (e.g., different subreddits), each has its own file

## Simplification: Remove Checkpoint System

Cache replaces the checkpoint system's resumability:
- If interrupted, re-run → cached posts are instant, only remaining posts call LLM

**Remove from `summarize_subreddit.py`:**
- `--checkpoint` option
- `--checkpoint-interval` option

**Remove from `summarizer.py`:**
- `_load_checkpoint()` method
- `_save_checkpoint()` method
- `_delete_checkpoint()` method
- Checkpoint-related parameters and logic in `generate_digest()`

**Remove from documentation:**
- `CLAUDE.md`: checkpoint references
- `docs/QUICK_START.md`: Tip 2 about checkpoints
- `docs/TECHNICAL.md`: checkpoint options

## Implementation Order
1. Create `cache.py` (standalone, no dependencies)
2. Update `__init__.py` exports
3. Update `summarizer.py`:
   - Add cache integration
   - Remove checkpoint methods and logic
4. Update `summarize_subreddit.py`:
   - Add `--cache/--no-cache` and `--cache-dir` options
   - Remove `--checkpoint` and `--checkpoint-interval` options
5. Update `.gitignore` (add `cache/`)
6. Update documentation (remove checkpoint references)
7. Create/update tests

## Verification
1. **Unit tests**: `uv run pytest tests/test_cache.py -v`
2. **Manual test (first run - cache enabled by default)**:
   ```bash
   uv run python summarize_subreddit.py Fire --timeframe week --summarize --max-posts 3
   # Should see: "Cache: 0 hits, 3 misses"
   ```
3. **Manual test (second run - should hit cache)**:
   ```bash
   uv run python summarize_subreddit.py Fire --timeframe week --summarize --max-posts 3
   # Should see: "Cache: 3 hits, 0 misses" (much faster, no LLM calls)
   ```
4. **Manual test with cache disabled**:
   ```bash
   uv run python summarize_subreddit.py Fire --timeframe week --summarize --max-posts 3 --no-cache
   # Should skip cache entirely, always call LLM
   ```
5. **Verify cache file created**: `cat cache/fire.json`
