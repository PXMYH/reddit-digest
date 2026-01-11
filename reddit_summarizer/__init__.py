"""
Reddit Subreddit Summarizer with ACE Framework

A tool to generate reading digests from Reddit subreddits using AI summarization
with self-improving capabilities through the Agentic Context Engineering framework.
"""

__version__ = "0.1.0"

# Always available - no dependencies
from .models import RedditPost, PostSummary, SubredditDigest
from .cache import SummaryCache

# Import optional components with graceful fallback
__all__ = ["RedditPost", "PostSummary", "SubredditDigest", "SummaryCache"]

try:
    from .fetcher import RedditFetcher

    __all__.append("RedditFetcher")
except ImportError as e:
    import warnings

    warnings.warn(
        f"RedditFetcher not available: {e}. Install with: pip install requests", ImportWarning
    )
    RedditFetcher = None  # type: ignore

try:
    from .summarizer import RedditSummarizer

    __all__.append("RedditSummarizer")
except ImportError as e:
    import warnings

    warnings.warn(
        f"RedditSummarizer not available: {e}. Install with: pip install ace-framework",
        ImportWarning,
    )
    RedditSummarizer = None  # type: ignore
