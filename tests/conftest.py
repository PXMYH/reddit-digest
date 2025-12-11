"""Pytest configuration and fixtures"""

import pytest
from datetime import datetime
from reddit_summarizer.models import RedditPost, PostSummary


@pytest.fixture
def sample_post():
    """Fixture for a sample Reddit post"""
    return RedditPost(
        title="Sample Post Title",
        author="test_user",
        url="https://reddit.com/test",
        selftext="This is a sample post content for testing.",
        score=250,
        num_comments=75,
        created_utc=datetime(2024, 1, 15, 12, 30),
        permalink="/r/test/comments/abc123/sample_post_title/",
        post_id="abc123",
        subreddit="test",
    )


@pytest.fixture
def sample_post_list():
    """Fixture for a list of sample Reddit posts"""
    posts = []
    for i in range(5):
        post = RedditPost(
            title=f"Test Post {i+1}",
            author=f"user_{i+1}",
            url=f"https://reddit.com/test{i+1}",
            selftext=f"Content for post {i+1}",
            score=100 + (i * 50),
            num_comments=30 + (i * 10),
            created_utc=datetime(2024, 1, i + 1),
            permalink=f"/r/test/comments/id{i+1}/test_post_{i+1}/",
            post_id=f"id{i+1}",
            subreddit="test",
        )
        posts.append(post)
    return posts


@pytest.fixture
def sample_summary(sample_post):
    """Fixture for a sample post summary"""
    return PostSummary(
        post=sample_post,
        summary="This is a concise summary of the post.",
        key_points=["Point 1", "Point 2", "Point 3"],
        discussion_highlights="Active discussion about testing strategies.",
    )
