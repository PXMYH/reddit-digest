"""Tests for SummaryCache"""

import json
import pytest
from datetime import datetime
from pathlib import Path

from reddit_summarizer.cache import SummaryCache
from reddit_summarizer.models import RedditPost, PostSummary


@pytest.fixture
def sample_post():
    """Create a sample RedditPost for testing."""
    return RedditPost(
        title="Test Post Title",
        author="test_user",
        url="https://reddit.com/r/test/comments/abc123/test/",
        selftext="This is test content for the post.",
        score=100,
        num_comments=50,
        created_utc=datetime(2024, 1, 15, 12, 0, 0),
        permalink="/r/test/comments/abc123/test/",
        post_id="abc123",
        subreddit="test",
    )


@pytest.fixture
def sample_summary(sample_post):
    """Create a sample PostSummary for testing."""
    return PostSummary(
        post=sample_post,
        summary="This is a test summary of the post.",
        key_points=["Point 1", "Point 2", "Point 3"],
        discussion_highlights="The discussion was lively.",
    )


class TestSummaryCache:
    """Tests for SummaryCache class."""

    def test_cache_miss_returns_none(self, tmp_path):
        """Test that cache miss returns None."""
        cache = SummaryCache(cache_dir=str(tmp_path))
        cache.load("test")
        result = cache.get("test", "nonexistent_post_id")
        assert result is None

    def test_put_and_get(self, tmp_path, sample_summary):
        """Test storing and retrieving a summary."""
        cache = SummaryCache(cache_dir=str(tmp_path))
        cache.load("test")

        # Store summary
        cache.put("test", "abc123", sample_summary)

        # Retrieve summary
        result = cache.get("test", "abc123")

        assert result is not None
        assert result["summary"] == "This is a test summary of the post."
        assert result["key_points"] == ["Point 1", "Point 2", "Point 3"]
        assert result["discussion_highlights"] == "The discussion was lively."

    def test_save_and_load(self, tmp_path, sample_summary):
        """Test saving cache to disk and loading it back."""
        # Save cache
        cache1 = SummaryCache(cache_dir=str(tmp_path))
        cache1.load("test")
        cache1.put("test", "abc123", sample_summary)
        cache1.save("test")

        # Load in new instance
        cache2 = SummaryCache(cache_dir=str(tmp_path))
        cache2.load("test")

        result = cache2.get("test", "abc123")
        assert result is not None
        assert result["summary"] == "This is a test summary of the post."
        assert result["key_points"] == ["Point 1", "Point 2", "Point 3"]

    def test_cache_file_created(self, tmp_path, sample_summary):
        """Test that cache file is created with correct name."""
        cache = SummaryCache(cache_dir=str(tmp_path))
        cache.load("TestSubreddit")
        cache.put("TestSubreddit", "abc123", sample_summary)
        cache.save("TestSubreddit")

        # Check file exists (lowercase)
        cache_file = tmp_path / "testsubreddit.json"
        assert cache_file.exists()

        # Verify content
        with open(cache_file) as f:
            data = json.load(f)
        assert "abc123" in data

    def test_cache_stats(self, tmp_path, sample_summary):
        """Test cache statistics tracking."""
        cache = SummaryCache(cache_dir=str(tmp_path))
        cache.load("test")

        # Initial stats
        stats = cache.get_stats("test")
        assert stats["hits"] == 0
        assert stats["misses"] == 0
        assert stats["cached_posts"] == 0

        # Add some entries
        cache.put("test", "post1", sample_summary)
        cache.put("test", "post2", sample_summary)

        # Check cached posts count
        stats = cache.get_stats("test")
        assert stats["cached_posts"] == 2

    def test_cache_hit_increments_stats(self, tmp_path, sample_summary):
        """Test that cache hits increment stats."""
        cache = SummaryCache(cache_dir=str(tmp_path))
        cache.load("test")
        cache.put("test", "abc123", sample_summary)

        # Cache hit
        cache.get("test", "abc123")
        cache.get("test", "abc123")

        stats = cache.get_stats("test")
        assert stats["hits"] == 2

    def test_cache_miss_increments_stats(self, tmp_path):
        """Test that cache misses increment stats."""
        cache = SummaryCache(cache_dir=str(tmp_path))
        cache.load("test")

        # Cache misses
        cache.get("test", "nonexistent1")
        cache.get("test", "nonexistent2")

        stats = cache.get_stats("test")
        assert stats["misses"] == 2

    def test_corrupted_cache_handled(self, tmp_path):
        """Test that corrupted cache file is handled gracefully."""
        # Write corrupted JSON
        cache_dir = tmp_path
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_file = cache_dir / "test.json"
        cache_file.write_text("not valid json {{{")

        cache = SummaryCache(cache_dir=str(tmp_path))
        cache.load("test")  # Should not raise

        # Cache should be empty after failed load
        assert cache.get("test", "any") is None

    def test_case_insensitive_subreddit(self, tmp_path, sample_summary):
        """Test that subreddit names are case-insensitive."""
        cache = SummaryCache(cache_dir=str(tmp_path))

        # Load with uppercase
        cache.load("TestSubreddit")
        cache.put("TestSubreddit", "abc123", sample_summary)
        cache.save("TestSubreddit")

        # Load with lowercase in new instance
        cache2 = SummaryCache(cache_dir=str(tmp_path))
        cache2.load("testsubreddit")

        result = cache2.get("testsubreddit", "abc123")
        assert result is not None

    def test_auto_load_on_get(self, tmp_path, sample_summary):
        """Test that get() auto-loads cache if not loaded."""
        # First, create and save a cache
        cache1 = SummaryCache(cache_dir=str(tmp_path))
        cache1.load("test")
        cache1.put("test", "abc123", sample_summary)
        cache1.save("test")

        # Create new cache without explicit load
        cache2 = SummaryCache(cache_dir=str(tmp_path))
        # get() should auto-load
        result = cache2.get("test", "abc123")
        assert result is not None

    def test_cache_directory_created(self, tmp_path):
        """Test that cache directory is created if it doesn't exist."""
        cache_dir = tmp_path / "new_cache_dir"
        assert not cache_dir.exists()

        cache = SummaryCache(cache_dir=str(cache_dir))
        cache.load("test")
        cache.put("test", "abc123", PostSummary(
            post=RedditPost(
                title="Test", author="user", url="https://reddit.com",
                selftext="", score=1, num_comments=0,
                created_utc=datetime.now(), permalink="/r/test",
                post_id="abc123", subreddit="test"
            ),
            summary="Test summary",
            key_points=[],
            discussion_highlights=""
        ))
        cache.save("test")

        assert cache_dir.exists()
        assert (cache_dir / "test.json").exists()
