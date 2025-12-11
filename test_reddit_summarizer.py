#!/usr/bin/env python3
"""
Unit tests for Reddit Summarizer

Following learned strategies:
- [testing-00021] Mock external dependencies in sys.modules
- [testing-00022] Use pytest fixtures to reduce duplication
"""

import unittest
from unittest.mock import Mock, MagicMock, patch
from datetime import datetime, timedelta
import sys

# Mock PRAW before importing reddit_summarizer
sys.modules['praw'] = MagicMock()

from reddit_summarizer import (
    RedditPost,
    RedditSummarizer,
    parse_date,
    convert_to_html,
)


class TestRedditPost(unittest.TestCase):
    """Test RedditPost dataclass."""

    def test_post_creation(self):
        """Test creating a RedditPost."""
        post = RedditPost(
            title="Test Post",
            author="test_user",
            score=150,
            num_comments=50,
            url="https://reddit.com/r/test/post",
            created_utc=1702368000.0,  # 2023-12-12
            selftext="Test content",
            permalink="https://reddit.com/r/test/comments/abc123",
        )

        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.score, 150)
        self.assertEqual(post.num_comments, 50)

    def test_created_datetime_property(self):
        """Test datetime conversion from Unix timestamp."""
        post = RedditPost(
            title="Test",
            author="user",
            score=100,
            num_comments=30,
            url="",
            created_utc=1702368000.0,
            selftext="",
            permalink="",
        )

        dt = post.created_datetime
        self.assertIsInstance(dt, datetime)
        self.assertEqual(dt.year, 2023)
        self.assertEqual(dt.month, 12)

    def test_repr(self):
        """Test string representation."""
        post = RedditPost(
            title="A" * 60,  # Long title
            author="user",
            score=200,
            num_comments=100,
            url="",
            created_utc=0,
            selftext="",
            permalink="",
        )

        repr_str = repr(post)
        self.assertIn("score=200", repr_str)
        self.assertIn("comments=100", repr_str)
        # Should truncate long title
        self.assertTrue(len(repr_str) < 150)


class TestRedditSummarizer(unittest.TestCase):
    """Test RedditSummarizer class."""

    def setUp(self):
        """Set up test fixtures [testing-00022]."""
        self.summarizer = RedditSummarizer(
            min_upvotes=100,
            min_comments=30,
            max_posts=50,
        )

    def test_initialization(self):
        """Test summarizer initialization."""
        self.assertEqual(self.summarizer.min_upvotes, 100)
        self.assertEqual(self.summarizer.min_comments, 30)
        self.assertEqual(self.summarizer.max_posts, 50)
        self.assertIsNone(self.summarizer.reddit)
        self.assertIsNone(self.summarizer.llm_client)

    def test_initialization_with_llm(self):
        """Test summarizer with LLM client."""
        mock_llm = Mock()
        summarizer = RedditSummarizer(llm_client=mock_llm)
        self.assertEqual(summarizer.llm_client, mock_llm)

    @patch('reddit_summarizer.praw')
    def test_connect(self, mock_praw):
        """Test Reddit API connection."""
        mock_reddit = MagicMock()
        mock_reddit.read_only = True
        mock_praw.Reddit.return_value = mock_reddit

        self.summarizer.connect("client_id", "secret", "user_agent")

        mock_praw.Reddit.assert_called_once()
        self.assertEqual(self.summarizer.reddit, mock_reddit)

    def test_generate_text_summary_empty(self):
        """Test text summary with no posts."""
        summary = self.summarizer.generate_text_summary([])
        self.assertIn("No important posts found", summary)

    def test_generate_text_summary_with_posts(self):
        """Test text summary with posts."""
        posts = [
            RedditPost(
                title="Test Post 1",
                author="user1",
                score=150,
                num_comments=50,
                url="https://reddit.com",
                created_utc=datetime.now().timestamp(),
                selftext="Content here",
                permalink="https://reddit.com/r/test/1",
            ),
            RedditPost(
                title="Test Post 2",
                author="user2",
                score=200,
                num_comments=80,
                url="https://reddit.com",
                created_utc=datetime.now().timestamp(),
                selftext="",
                permalink="https://reddit.com/r/test/2",
            ),
        ]

        summary = self.summarizer.generate_text_summary(posts)

        self.assertIn("Total Important Posts: 2", summary)
        self.assertIn("Test Post 1", summary)
        self.assertIn("Test Post 2", summary)
        self.assertIn("user1", summary)
        self.assertIn("user2", summary)
        self.assertIn("150 upvotes", summary)

    def test_generate_llm_summary_without_llm(self):
        """Test LLM summary falls back to text summary when no LLM."""
        posts = [
            RedditPost(
                title="Test",
                author="user",
                score=100,
                num_comments=30,
                url="",
                created_utc=0,
                selftext="",
                permalink="",
            )
        ]

        summary = self.summarizer.generate_llm_summary(posts, "test")
        # Should fall back to text summary
        self.assertIn("REDDIT SUBREDDIT DIGEST", summary)

    def test_generate_llm_summary_with_llm(self):
        """Test LLM summary generation."""
        mock_llm = Mock()
        mock_llm.complete.return_value = "## Key Themes\nTest analysis"

        self.summarizer.llm_client = mock_llm

        posts = [
            RedditPost(
                title="Test Post",
                author="user",
                score=150,
                num_comments=50,
                url="",
                created_utc=datetime.now().timestamp(),
                selftext="Content",
                permalink="https://reddit.com/test",
            )
        ]

        summary = self.summarizer.generate_llm_summary(posts, "python")

        mock_llm.complete.assert_called_once()
        self.assertIn("AI-POWERED REDDIT DIGEST", summary)
        self.assertIn("r/python", summary)
        self.assertIn("Test Post", summary)

    def test_generate_llm_summary_handles_errors(self):
        """Test LLM summary handles errors gracefully."""
        mock_llm = Mock()
        mock_llm.complete.side_effect = Exception("API Error")

        self.summarizer.llm_client = mock_llm

        posts = [
            RedditPost(
                title="Test",
                author="user",
                score=100,
                num_comments=30,
                url="",
                created_utc=0,
                selftext="",
                permalink="",
            )
        ]

        summary = self.summarizer.generate_llm_summary(posts, "test")
        # Should fall back to text summary on error
        self.assertIn("REDDIT SUBREDDIT DIGEST", summary)


class TestHelperFunctions(unittest.TestCase):
    """Test helper functions."""

    def test_parse_date_valid(self):
        """Test parsing valid date."""
        dt = parse_date("2024-12-10")
        self.assertEqual(dt.year, 2024)
        self.assertEqual(dt.month, 12)
        self.assertEqual(dt.day, 10)

    def test_parse_date_invalid(self):
        """Test parsing invalid date."""
        with self.assertRaises(SystemExit):
            parse_date("invalid-date")

    def test_convert_to_html_basic(self):
        """Test HTML conversion."""
        text = "Test Summary\n\nSome content"
        start_date = datetime(2024, 12, 1)
        end_date = datetime(2024, 12, 10)

        html = convert_to_html(text, "python", start_date, end_date)

        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("r/python", html)
        self.assertIn("December 01, 2024", html)
        self.assertIn("December 10, 2024", html)
        self.assertIn("Test Summary", html)

    def test_convert_to_html_with_links(self):
        """Test HTML conversion preserves links."""
        text = "Check https://reddit.com/r/test"
        start_date = datetime.now()
        end_date = datetime.now()

        html = convert_to_html(text, "test", start_date, end_date)

        self.assertIn('<a href="https://reddit.com/r/test"', html)
        self.assertIn('target="_blank"', html)

    def test_convert_to_html_escapes_special_chars(self):
        """Test HTML conversion escapes special characters."""
        text = "Test <script>alert('xss')</script>"
        start_date = datetime.now()
        end_date = datetime.now()

        html = convert_to_html(text, "test", start_date, end_date)

        # Should escape HTML tags
        self.assertIn("&lt;script&gt;", html)
        self.assertIn("&lt;/script&gt;", html)
        # Should not contain unescaped tags
        self.assertNotIn("<script>alert", html)


class TestIntegration(unittest.TestCase):
    """Integration tests for complete workflows."""

    def test_full_workflow_without_llm(self):
        """Test complete summarization workflow."""
        summarizer = RedditSummarizer()

        posts = [
            RedditPost(
                title=f"Post {i}",
                author=f"user{i}",
                score=100 + i * 10,
                num_comments=30 + i * 5,
                url=f"https://reddit.com/{i}",
                created_utc=datetime.now().timestamp(),
                selftext=f"Content {i}",
                permalink=f"https://reddit.com/r/test/{i}",
            )
            for i in range(5)
        ]

        summary = summarizer.generate_text_summary(posts)

        self.assertIn("Total Important Posts: 5", summary)
        for i in range(5):
            self.assertIn(f"Post {i}", summary)


if __name__ == "__main__":
    # Run tests with verbose output [testing-00013]
    unittest.main(verbosity=2)
