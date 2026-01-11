"""
Summary cache for avoiding re-summarization of previously processed posts.

Cache is stored as JSON files per subreddit in the cache directory.
"""

import json
import logging
from pathlib import Path
from typing import Optional

from .models import PostSummary, RedditPost

logger = logging.getLogger(__name__)


class SummaryCache:
    """Simple JSON-based cache for post summaries, keyed by post_id."""

    def __init__(self, cache_dir: str = "cache"):
        """Initialize the cache.

        Args:
            cache_dir: Directory to store cache files. Created if it doesn't exist.
        """
        self.cache_dir = Path(cache_dir)
        self._caches: dict[str, dict] = {}  # {subreddit: {post_id: summary_data}}
        self._stats: dict[str, dict] = {}  # {subreddit: {hits: int, misses: int}}

    def load(self, subreddit: str) -> None:
        """Load cache for a subreddit from disk.

        Args:
            subreddit: Name of the subreddit (case-insensitive, stored lowercase).
        """
        subreddit_key = subreddit.lower()
        cache_file = self.cache_dir / f"{subreddit_key}.json"

        self._stats[subreddit_key] = {"hits": 0, "misses": 0}

        if not cache_file.exists():
            self._caches[subreddit_key] = {}
            return

        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                self._caches[subreddit_key] = json.load(f)
            logger.info(
                f"Loaded {len(self._caches[subreddit_key])} cached summaries for r/{subreddit}"
            )
        except (json.JSONDecodeError, IOError) as e:
            logger.warning(f"Failed to load cache for r/{subreddit}: {e}. Starting fresh.")
            self._caches[subreddit_key] = {}

    def get(self, subreddit: str, post_id: str) -> Optional[dict]:
        """Get cached summary data for a post.

        Args:
            subreddit: Name of the subreddit.
            post_id: Reddit post ID.

        Returns:
            Dict with summary, key_points, discussion_highlights if cached, else None.
        """
        subreddit_key = subreddit.lower()

        if subreddit_key not in self._caches:
            self.load(subreddit)

        cached = self._caches.get(subreddit_key, {}).get(post_id)

        if cached:
            self._stats[subreddit_key]["hits"] += 1
        else:
            self._stats[subreddit_key]["misses"] += 1

        return cached

    def put(self, subreddit: str, post_id: str, summary: PostSummary) -> None:
        """Store a summary in the cache.

        Args:
            subreddit: Name of the subreddit.
            post_id: Reddit post ID.
            summary: PostSummary object to cache.
        """
        subreddit_key = subreddit.lower()

        if subreddit_key not in self._caches:
            self._caches[subreddit_key] = {}

        self._caches[subreddit_key][post_id] = {
            "summary": summary.summary,
            "key_points": summary.key_points,
            "discussion_highlights": summary.discussion_highlights,
        }

    def save(self, subreddit: str) -> None:
        """Save cache for a subreddit to disk.

        Args:
            subreddit: Name of the subreddit.
        """
        subreddit_key = subreddit.lower()

        if subreddit_key not in self._caches:
            return

        # Create cache directory if it doesn't exist
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        cache_file = self.cache_dir / f"{subreddit_key}.json"

        try:
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(self._caches[subreddit_key], f, indent=2)
            logger.info(
                f"Saved {len(self._caches[subreddit_key])} summaries to cache for r/{subreddit}"
            )
        except IOError as e:
            logger.warning(f"Failed to save cache for r/{subreddit}: {e}")

    def get_stats(self, subreddit: str) -> dict:
        """Get cache statistics for a subreddit.

        Args:
            subreddit: Name of the subreddit.

        Returns:
            Dict with hits, misses, and cached_posts counts.
        """
        subreddit_key = subreddit.lower()
        stats = self._stats.get(subreddit_key, {"hits": 0, "misses": 0})
        cached_posts = len(self._caches.get(subreddit_key, {}))

        return {
            "hits": stats["hits"],
            "misses": stats["misses"],
            "cached_posts": cached_posts,
        }
