"""Integration tests for Reddit fetcher with mocked API"""

import pytest
from datetime import datetime
from unittest.mock import Mock, MagicMock, patch
from reddit_summarizer.models import RedditPost


# Only run these tests if praw is available
pytest.importorskip("praw")

from reddit_summarizer.fetcher import RedditFetcher


class TestRedditFetcher:
    """Tests for RedditFetcher with mocked PRAW"""

    @pytest.fixture
    def mock_reddit(self):
        """Mock PRAW Reddit instance"""
        with patch("reddit_summarizer.fetcher.praw.Reddit") as mock:
            yield mock

    @pytest.fixture
    def fetcher(self, mock_reddit):
        """Create a fetcher with mocked credentials"""
        with patch.dict("os.environ", {"REDDIT_CLIENT_ID": "test", "REDDIT_CLIENT_SECRET": "test"}):
            return RedditFetcher()

    def test_initialization_with_env_vars(self, mock_reddit):
        """Test fetcher initialization with environment variables"""
        with patch.dict(
            "os.environ",
            {
                "REDDIT_CLIENT_ID": "test_id",
                "REDDIT_CLIENT_SECRET": "test_secret",
                "REDDIT_USER_AGENT": "TestAgent/1.0",
            },
        ):
            fetcher = RedditFetcher()
            assert fetcher.client_id == "test_id"
            assert fetcher.client_secret == "test_secret"
            assert fetcher.user_agent == "TestAgent/1.0"

    def test_initialization_with_params(self, mock_reddit):
        """Test fetcher initialization with explicit parameters"""
        fetcher = RedditFetcher(
            client_id="param_id", client_secret="param_secret", user_agent="ParamAgent/1.0"
        )
        assert fetcher.client_id == "param_id"
        assert fetcher.client_secret == "param_secret"
        assert fetcher.user_agent == "ParamAgent/1.0"

    def test_initialization_missing_credentials(self, mock_reddit):
        """Test that initialization fails without credentials"""
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError, match="Reddit API credentials not provided"):
                RedditFetcher()

    def test_fetch_posts_basic(self, fetcher, mock_reddit):
        """Test basic post fetching with mocked data"""
        # Create mock submission
        mock_submission = Mock()
        mock_submission.title = "Test Post"
        mock_submission.author = "test_user"
        mock_submission.url = "https://example.com"
        mock_submission.selftext = "Test content"
        mock_submission.score = 150
        mock_submission.num_comments = 50
        mock_submission.created_utc = datetime(2024, 1, 15).timestamp()
        mock_submission.permalink = "/r/test/comments/123/test_post/"
        mock_submission.id = "123"

        # Mock subreddit
        mock_subreddit = Mock()
        mock_subreddit.id = "test_sub_id"
        mock_subreddit.top.return_value = [mock_submission]

        # Setup mock reddit
        fetcher.reddit.subreddit.return_value = mock_subreddit

        # Fetch posts
        posts = fetcher.fetch_posts(
            subreddit_name="test",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31),
            min_upvotes=100,
            min_comments=30,
            max_posts=10,
        )

        assert len(posts) == 1
        assert posts[0].title == "Test Post"
        assert posts[0].score == 150
        assert posts[0].num_comments == 50

    def test_fetch_posts_filtering(self, fetcher, mock_reddit):
        """Test that posts are filtered by thresholds"""
        # Create mock submissions with different scores
        mock_submission1 = Mock()
        mock_submission1.score = 50  # Below threshold
        mock_submission1.num_comments = 25  # Below threshold
        mock_submission1.created_utc = datetime(2024, 1, 15).timestamp()

        mock_submission2 = Mock()
        mock_submission2.title = "Valid Post"
        mock_submission2.author = "test_user"
        mock_submission2.url = "https://example.com"
        mock_submission2.selftext = "Test"
        mock_submission2.score = 200  # Above threshold
        mock_submission2.num_comments = 50  # Above threshold
        mock_submission2.created_utc = datetime(2024, 1, 15).timestamp()
        mock_submission2.permalink = "/r/test/comments/456/valid_post/"
        mock_submission2.id = "456"

        # Mock subreddit
        mock_subreddit = Mock()
        mock_subreddit.id = "test_sub_id"
        mock_subreddit.top.return_value = [mock_submission1, mock_submission2]

        fetcher.reddit.subreddit.return_value = mock_subreddit

        # Fetch with thresholds
        posts = fetcher.fetch_posts(
            subreddit_name="test",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31),
            min_upvotes=100,
            min_comments=30,
            max_posts=10,
        )

        # Should only return the valid post
        assert len(posts) == 1
        assert posts[0].title == "Valid Post"

    def test_fetch_posts_date_filtering(self, fetcher, mock_reddit):
        """Test that posts are filtered by date range"""
        # Create posts outside and inside date range
        mock_submission1 = Mock()
        mock_submission1.score = 150
        mock_submission1.num_comments = 50
        mock_submission1.created_utc = datetime(2023, 12, 31).timestamp()  # Before range

        mock_submission2 = Mock()
        mock_submission2.title = "In Range"
        mock_submission2.author = "test_user"
        mock_submission2.url = "https://example.com"
        mock_submission2.selftext = "Test"
        mock_submission2.score = 150
        mock_submission2.num_comments = 50
        mock_submission2.created_utc = datetime(2024, 1, 15).timestamp()  # In range
        mock_submission2.permalink = "/r/test/comments/789/in_range/"
        mock_submission2.id = "789"

        mock_submission3 = Mock()
        mock_submission3.score = 150
        mock_submission3.num_comments = 50
        mock_submission3.created_utc = datetime(2024, 2, 1).timestamp()  # After range

        # Mock subreddit
        mock_subreddit = Mock()
        mock_subreddit.id = "test_sub_id"
        mock_subreddit.top.return_value = [mock_submission1, mock_submission2, mock_submission3]

        fetcher.reddit.subreddit.return_value = mock_subreddit

        # Fetch with date range
        posts = fetcher.fetch_posts(
            subreddit_name="test",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31),
            min_upvotes=100,
            min_comments=30,
            max_posts=10,
        )

        # Should only return the post in range
        assert len(posts) == 1
        assert posts[0].title == "In Range"

    def test_fetch_posts_max_limit(self, fetcher, mock_reddit):
        """Test that max_posts limit is respected"""
        # Create 5 mock submissions
        mock_submissions = []
        for i in range(5):
            mock_sub = Mock()
            mock_sub.title = f"Post {i}"
            mock_sub.author = "test_user"
            mock_sub.url = "https://example.com"
            mock_sub.selftext = "Test"
            mock_sub.score = 150
            mock_sub.num_comments = 50
            mock_sub.created_utc = datetime(2024, 1, i + 1).timestamp()
            mock_sub.permalink = f"/r/test/comments/{i}/post_{i}/"
            mock_sub.id = str(i)
            mock_submissions.append(mock_sub)

        # Mock subreddit
        mock_subreddit = Mock()
        mock_subreddit.id = "test_sub_id"
        mock_subreddit.top.return_value = mock_submissions

        fetcher.reddit.subreddit.return_value = mock_subreddit

        # Fetch with max_posts=3
        posts = fetcher.fetch_posts(
            subreddit_name="test",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31),
            min_upvotes=100,
            min_comments=30,
            max_posts=3,
        )

        # Should return exactly 3 posts
        assert len(posts) == 3

    def test_fetch_posts_invalid_subreddit(self, fetcher):
        """Test handling of invalid subreddit"""
        from prawcore.exceptions import NotFound

        fetcher.reddit.subreddit.side_effect = NotFound(Mock())

        with pytest.raises(NotFound):
            fetcher.fetch_posts(
                subreddit_name="nonexistent",
                start_date=datetime(2024, 1, 1),
                end_date=datetime(2024, 1, 31),
            )

    def test_fetch_posts_invalid_params(self, fetcher):
        """Test validation of input parameters"""
        # Empty subreddit name
        with pytest.raises(ValueError, match="Subreddit name cannot be empty"):
            fetcher.fetch_posts(
                subreddit_name="",
                start_date=datetime(2024, 1, 1),
                end_date=datetime(2024, 1, 31),
            )

        # Start date after end date
        with pytest.raises(ValueError, match="Start date must be before end date"):
            fetcher.fetch_posts(
                subreddit_name="test",
                start_date=datetime(2024, 1, 31),
                end_date=datetime(2024, 1, 1),
            )

        # Negative thresholds
        with pytest.raises(ValueError, match="Thresholds cannot be negative"):
            fetcher.fetch_posts(
                subreddit_name="test",
                start_date=datetime(2024, 1, 1),
                end_date=datetime(2024, 1, 31),
                min_upvotes=-10,
            )

    def test_fetch_post_comments(self, fetcher, mock_reddit):
        """Test fetching comments for a post"""
        # Create mock comment
        mock_comment = Mock()
        mock_comment.author = "commenter"
        mock_comment.body = "Great post!"
        mock_comment.score = 25

        # Mock submission
        mock_submission = Mock()
        mock_submission.comment_sort = "top"
        mock_submission.comment_limit = 10
        mock_submission.comments = [mock_comment]

        fetcher.reddit.submission.return_value = mock_submission

        # Create a sample post
        post = RedditPost(
            title="Test",
            author="test_user",
            url="https://reddit.com/test",
            selftext="Content",
            score=100,
            num_comments=50,
            created_utc=datetime.now(),
            permalink="/r/test/comments/123/test/",
            post_id="123",
            subreddit="test",
        )

        # Fetch comments
        comments = fetcher.fetch_post_comments(post, limit=10)

        assert len(comments) == 1
        assert comments[0]["author"] == "commenter"
        assert comments[0]["body"] == "Great post!"
        assert comments[0]["score"] == 25

    def test_fetch_post_comments_invalid_limit(self, fetcher):
        """Test that invalid comment limit raises error"""
        post = RedditPost(
            title="Test",
            author="test_user",
            url="https://reddit.com/test",
            selftext="Content",
            score=100,
            num_comments=50,
            created_utc=datetime.now(),
            permalink="/r/test/comments/123/test/",
            post_id="123",
            subreddit="test",
        )

        with pytest.raises(ValueError, match="limit must be positive"):
            fetcher.fetch_post_comments(post, limit=0)
