"""Unit tests for Reddit fetcher timeframe functionality"""

import pytest
from datetime import datetime
from unittest.mock import Mock, patch, MagicMock
from reddit_summarizer.fetcher import RedditFetcher
from reddit_summarizer.models import RedditPost


class TestFetchPostsByTimeframe:
    """Tests for fetch_posts_by_timeframe method"""

    @pytest.fixture
    def fetcher(self):
        """Create a RedditFetcher instance"""
        return RedditFetcher()

    @pytest.fixture
    def mock_reddit_response(self):
        """Mock Reddit API response"""
        return {
            "data": {
                "children": [
                    {
                        "data": {
                            "title": "Test Post 1",
                            "author": "user1",
                            "url": "https://example.com/1",
                            "selftext": "Content 1",
                            "score": 200,
                            "num_comments": 50,
                            "created_utc": datetime(2024, 1, 15).timestamp(),
                            "permalink": "/r/test/comments/1/test_post_1/",
                            "id": "1",
                        }
                    },
                    {
                        "data": {
                            "title": "Test Post 2",
                            "author": "user2",
                            "url": "https://example.com/2",
                            "selftext": "Content 2",
                            "score": 150,
                            "num_comments": 40,
                            "created_utc": datetime(2024, 1, 14).timestamp(),
                            "permalink": "/r/test/comments/2/test_post_2/",
                            "id": "2",
                        }
                    },
                ],
                "after": None,  # No more pages
            }
        }

    def test_fetch_posts_by_timeframe_valid(self, fetcher, mock_reddit_response):
        """Test fetching posts with valid timeframe"""
        with patch.object(fetcher.session, 'get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_reddit_response
            mock_get.return_value = mock_response

            posts = fetcher.fetch_posts_by_timeframe(
                subreddit_name="test",
                timeframe="year",
                min_upvotes=100,
                min_comments=30,
                max_posts=10,
            )

            # Verify API call
            mock_get.assert_called_once()
            call_args = mock_get.call_args
            assert "test/top.json" in call_args[0][0]
            assert call_args[1]['params']['t'] == "year"

            # Verify results
            assert len(posts) == 2
            assert all(isinstance(p, RedditPost) for p in posts)
            assert posts[0].title == "Test Post 1"
            assert posts[0].score == 200

    def test_fetch_posts_by_timeframe_invalid_timeframe(self, fetcher):
        """Test error handling for invalid timeframe"""
        with pytest.raises(ValueError, match="Invalid timeframe"):
            fetcher.fetch_posts_by_timeframe(
                subreddit_name="test",
                timeframe="invalid",
            )

    def test_fetch_posts_by_timeframe_valid_timeframes(self, fetcher, mock_reddit_response):
        """Test all valid timeframes are accepted"""
        valid_timeframes = ["hour", "day", "week", "month", "year", "all"]

        with patch.object(fetcher.session, 'get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_reddit_response
            mock_get.return_value = mock_response

            for timeframe in valid_timeframes:
                posts = fetcher.fetch_posts_by_timeframe(
                    subreddit_name="test",
                    timeframe=timeframe,
                )
                assert isinstance(posts, list)

    def test_fetch_posts_by_timeframe_filters(self, fetcher):
        """Test upvote and comment thresholds are applied"""
        response = {
            "data": {
                "children": [
                    {
                        "data": {
                            "title": "High upvotes",
                            "author": "user1",
                            "url": "https://example.com/1",
                            "selftext": "",
                            "score": 500,  # Meets threshold
                            "num_comments": 100,  # Meets threshold
                            "created_utc": datetime.now().timestamp(),
                            "permalink": "/r/test/comments/1/",
                            "id": "1",
                        }
                    },
                    {
                        "data": {
                            "title": "Low upvotes",
                            "author": "user2",
                            "url": "https://example.com/2",
                            "selftext": "",
                            "score": 50,  # Below threshold
                            "num_comments": 100,
                            "created_utc": datetime.now().timestamp(),
                            "permalink": "/r/test/comments/2/",
                            "id": "2",
                        }
                    },
                    {
                        "data": {
                            "title": "Low comments",
                            "author": "user3",
                            "url": "https://example.com/3",
                            "selftext": "",
                            "score": 500,
                            "num_comments": 10,  # Below threshold
                            "created_utc": datetime.now().timestamp(),
                            "permalink": "/r/test/comments/3/",
                            "id": "3",
                        }
                    },
                ],
                "after": None,
            }
        }

        with patch.object(fetcher.session, 'get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = response
            mock_get.return_value = mock_response

            posts = fetcher.fetch_posts_by_timeframe(
                subreddit_name="test",
                timeframe="year",
                min_upvotes=100,
                min_comments=30,
            )

            # Only the first post should pass both thresholds
            assert len(posts) == 1
            assert posts[0].title == "High upvotes"

    def test_fetch_posts_by_timeframe_pagination(self, fetcher):
        """Test pagination support"""
        # First page
        response_page1 = {
            "data": {
                "children": [
                    {
                        "data": {
                            "title": f"Post {i}",
                            "author": "user",
                            "url": f"https://example.com/{i}",
                            "selftext": "",
                            "score": 200,
                            "num_comments": 50,
                            "created_utc": datetime.now().timestamp(),
                            "permalink": f"/r/test/comments/{i}/",
                            "id": str(i),
                        }
                    }
                    for i in range(5)
                ],
                "after": "page2_token",
            }
        }

        # Second page
        response_page2 = {
            "data": {
                "children": [
                    {
                        "data": {
                            "title": f"Post {i}",
                            "author": "user",
                            "url": f"https://example.com/{i}",
                            "selftext": "",
                            "score": 200,
                            "num_comments": 50,
                            "created_utc": datetime.now().timestamp(),
                            "permalink": f"/r/test/comments/{i}/",
                            "id": str(i),
                        }
                    }
                    for i in range(5, 8)
                ],
                "after": None,
            }
        }

        with patch.object(fetcher.session, 'get') as mock_get:
            mock_response1 = Mock()
            mock_response1.status_code = 200
            mock_response1.json.return_value = response_page1

            mock_response2 = Mock()
            mock_response2.status_code = 200
            mock_response2.json.return_value = response_page2

            mock_get.side_effect = [mock_response1, mock_response2]

            posts = fetcher.fetch_posts_by_timeframe(
                subreddit_name="test",
                timeframe="year",
                max_posts=10,
            )

            # Should fetch from both pages
            assert mock_get.call_count == 2
            assert len(posts) == 8

    def test_fetch_posts_by_timeframe_empty_subreddit(self, fetcher):
        """Test handling of subreddit with no posts"""
        response = {"data": {"children": [], "after": None}}

        with patch.object(fetcher.session, 'get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = response
            mock_get.return_value = mock_response

            posts = fetcher.fetch_posts_by_timeframe(
                subreddit_name="test",
                timeframe="year",
            )

            assert len(posts) == 0

    def test_fetch_posts_by_timeframe_validation(self, fetcher):
        """Test input validation"""
        # Empty subreddit name
        with pytest.raises(ValueError, match="Subreddit name cannot be empty"):
            fetcher.fetch_posts_by_timeframe(
                subreddit_name="",
                timeframe="year",
            )

        # Negative thresholds
        with pytest.raises(ValueError, match="Thresholds cannot be negative"):
            fetcher.fetch_posts_by_timeframe(
                subreddit_name="test",
                timeframe="year",
                min_upvotes=-1,
            )

        # Invalid max_posts
        with pytest.raises(ValueError, match="max_posts must be positive"):
            fetcher.fetch_posts_by_timeframe(
                subreddit_name="test",
                timeframe="year",
                max_posts=0,
            )

    def test_fetch_posts_by_timeframe_404_error(self, fetcher):
        """Test handling of non-existent subreddit"""
        import requests

        with patch.object(fetcher.session, 'get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 404
            http_error = requests.HTTPError("404 Not Found")
            http_error.response = mock_response
            mock_response.raise_for_status.side_effect = http_error
            mock_get.return_value = mock_response

            with pytest.raises(ValueError, match="does not exist"):
                fetcher.fetch_posts_by_timeframe(
                    subreddit_name="nonexistent",
                    timeframe="year",
                )

    def test_fetch_posts_by_timeframe_sorting(self, fetcher):
        """Test that posts are sorted by creation date (newest first)"""
        response = {
            "data": {
                "children": [
                    {
                        "data": {
                            "title": "Older Post",
                            "author": "user1",
                            "url": "https://example.com/1",
                            "selftext": "",
                            "score": 200,
                            "num_comments": 50,
                            "created_utc": datetime(2024, 1, 10).timestamp(),
                            "permalink": "/r/test/comments/1/",
                            "id": "1",
                        }
                    },
                    {
                        "data": {
                            "title": "Newer Post",
                            "author": "user2",
                            "url": "https://example.com/2",
                            "selftext": "",
                            "score": 150,
                            "num_comments": 40,
                            "created_utc": datetime(2024, 1, 15).timestamp(),
                            "permalink": "/r/test/comments/2/",
                            "id": "2",
                        }
                    },
                ],
                "after": None,
            }
        }

        with patch.object(fetcher.session, 'get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = response
            mock_get.return_value = mock_response

            posts = fetcher.fetch_posts_by_timeframe(
                subreddit_name="test",
                timeframe="year",
            )

            # Newer post should be first (newest first)
            assert len(posts) == 2
            assert posts[0].title == "Newer Post"
            assert posts[1].title == "Older Post"
            assert posts[0].created_utc > posts[1].created_utc
