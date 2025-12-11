"""
Reddit Subreddit Summarizer with ACE Framework

A tool to generate reading digests from Reddit subreddits using AI summarization
with self-improving capabilities through the Agentic Context Engineering framework.
"""

__version__ = "0.1.0"

from .models import RedditPost, SubredditDigest
from .fetcher import RedditFetcher
from .summarizer import RedditSummarizer

__all__ = [
    "RedditPost",
    "SubredditDigest",
    "RedditFetcher",
    "RedditSummarizer",
]
