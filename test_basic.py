#!/usr/bin/env python3
"""
Basic tests for Reddit Summarizer

Run with: python test_basic.py
"""

from datetime import datetime
from reddit_summarizer.models import RedditPost, PostSummary, SubredditDigest


def test_reddit_post_model():
    """Test RedditPost data model"""
    print("Testing RedditPost model...")

    post = RedditPost(
        title="Test Post",
        author="testuser",
        url="https://reddit.com/test",
        selftext="This is a test post content",
        score=150,
        num_comments=50,
        created_utc=datetime(2024, 1, 15),
        permalink="/r/test/comments/abc123/test_post/",
        post_id="abc123",
        subreddit="test",
    )

    # Test threshold checking
    assert post.meets_threshold(100, 30) == True
    assert post.meets_threshold(200, 30) == False
    assert post.meets_threshold(100, 60) == False

    # Test URL generation
    assert post.full_url == "https://reddit.com/r/test/comments/abc123/test_post/"

    # Test dict conversion
    post_dict = post.to_dict()
    assert post_dict["title"] == "Test Post"
    assert post_dict["upvotes"] == 150
    assert post_dict["comments"] == 50

    print("  ✅ RedditPost model tests passed")


def test_post_summary_model():
    """Test PostSummary data model"""
    print("Testing PostSummary model...")

    post = RedditPost(
        title="Test Post",
        author="testuser",
        url="https://reddit.com/test",
        selftext="Test content",
        score=150,
        num_comments=50,
        created_utc=datetime(2024, 1, 15),
        permalink="/r/test/comments/abc123/test_post/",
        post_id="abc123",
        subreddit="test",
    )

    summary = PostSummary(
        post=post,
        summary="This is a test summary",
        key_points=["Point 1", "Point 2", "Point 3"],
        discussion_highlights="Good discussion about testing",
    )

    # Test markdown generation
    markdown = summary.to_markdown()
    assert "Test Post" in markdown
    assert "This is a test summary" in markdown
    assert "Point 1" in markdown
    assert "Good discussion" in markdown

    print("  ✅ PostSummary model tests passed")


def test_subreddit_digest_model():
    """Test SubredditDigest data model"""
    print("Testing SubredditDigest model...")

    post = RedditPost(
        title="Test Post",
        author="testuser",
        url="https://reddit.com/test",
        selftext="Test content",
        score=150,
        num_comments=50,
        created_utc=datetime(2024, 1, 15),
        permalink="/r/test/comments/abc123/test_post/",
        post_id="abc123",
        subreddit="test",
    )

    summary = PostSummary(
        post=post,
        summary="Test summary",
        key_points=["Point 1"],
    )

    digest = SubredditDigest(
        subreddit="test",
        start_date=datetime(2024, 1, 1),
        end_date=datetime(2024, 1, 31),
        post_summaries=[summary],
        total_posts_analyzed=10,
    )

    # Test markdown generation
    markdown = digest.to_markdown()
    assert "r/test Reading Digest" in markdown
    assert "2024-01-01" in markdown
    assert "2024-01-31" in markdown
    assert "**Posts Summarized:** 1" in markdown
    assert "**Total Posts Analyzed:** 10" in markdown

    print("  ✅ SubredditDigest model tests passed")


def main():
    """Run all tests"""
    print("\n🧪 Running Basic Tests\n")

    try:
        test_reddit_post_model()
        test_post_summary_model()
        test_subreddit_digest_model()

        print("\n✅ All tests passed!\n")
        return 0

    except AssertionError as e:
        print(f"\n❌ Test failed: {e}\n")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}\n")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
