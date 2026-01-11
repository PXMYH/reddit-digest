"""
ACE-powered Reddit post summarizer with self-improving capabilities
"""

import json
from datetime import datetime
from typing import List, Optional
from .models import RedditPost, PostSummary, SubredditDigest
from .fetcher import RedditFetcher
from .cache import SummaryCache

try:
    from tqdm import tqdm

    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False

    # Fallback: tqdm acts as a simple iterator
    def tqdm(iterable, **kwargs):
        return iterable


try:
    from ace import Skillbook, Agent, Reflector, SkillManager
    from ace.llm_providers.litellm_client import LiteLLMClient
    from ace.prompts_v2_1 import PromptManager
except ImportError:
    raise ImportError("ACE framework not installed. Install with: pip install ace-framework")


class RedditSummarizer:
    """
    Summarizes Reddit posts using ACE framework for self-improving summaries
    """

    def __init__(
        self,
        model: str = "openrouter/mistralai/devstral-2512:free",
        skillbook_path: Optional[str] = None,
        fetcher: Optional[RedditFetcher] = None,
        cache: Optional[SummaryCache] = None,
    ):
        """
        Initialize the summarizer with ACE components

        Args:
            model: LLM model to use (default: openrouter/mistralai/devstral-2512:free)
            skillbook_path: Path to load existing skillbook (optional)
            fetcher: RedditFetcher instance (optional, will create one if not provided)
            cache: SummaryCache instance for caching summaries (optional)
        """
        self.model = model
        self.fetcher = fetcher
        self.cache = cache

        # Initialize LLM client
        self.llm = LiteLLMClient(model=model)

        # Initialize or load skillbook
        if skillbook_path:
            self.skillbook = Skillbook.load_from_file(skillbook_path)
            print(f"Loaded skillbook from {skillbook_path}")
        else:
            self.skillbook = Skillbook()

        # Initialize ACE components with v2.1 prompts (recommended)
        prompt_mgr = PromptManager()
        self.agent = Agent(
            llm=self.llm,
            prompt_template=prompt_mgr.get_agent_prompt(),
        )
        self.reflector = Reflector(
            llm=self.llm,
            prompt_template=prompt_mgr.get_reflector_prompt(),
        )
        self.skill_manager = SkillManager(
            llm=self.llm,
            prompt_template=prompt_mgr.get_skill_manager_prompt(),
        )

    def summarize_post(self, post: RedditPost, include_comments: bool = True) -> PostSummary:
        """
        Generate a summary for a single Reddit post

        Args:
            post: RedditPost to summarize
            include_comments: Whether to fetch and include top comments (default: True)

        Returns:
            PostSummary with AI-generated summary and key points
        """
        # Fetch top comments if requested
        comments_text = ""
        if include_comments and self.fetcher:
            comments = self.fetcher.fetch_post_comments(post, limit=10)
            if comments:
                comments_text = "\n\nTop Comments:\n"
                for i, comment in enumerate(comments[:5], 1):
                    comments_text += (
                        f"{i}. [{comment['score']} upvotes] {comment['body'][:200]}...\n"
                    )

        # Prepare prompt for the agent
        task = f"""Summarize this Reddit post from r/{post.subreddit}:

Title: {post.title}
Author: u/{post.author}
Upvotes: {post.score} | Comments: {post.num_comments}

Content: {post.selftext[:2000] if post.selftext else "[Link post - no text content]"}
{comments_text}

Please provide:
1. A concise summary (2-3 sentences)
2. 3-5 key points from the post and discussion
3. Brief description of discussion highlights or consensus (if applicable)

Format your response as JSON:
{{
    "summary": "...",
    "key_points": ["point1", "point2", "point3"],
    "discussion_highlights": "..."
}}
"""

        # Use ACE agent to generate summary with skillbook context
        agent_output = self.agent.generate(
            question=task,
            context=None,
            skillbook=self.skillbook,
        )

        # Parse the response
        try:
            result = json.loads(agent_output.final_answer)
            summary = result.get("summary", "")
            key_points = result.get("key_points", [])
            discussion_highlights = result.get("discussion_highlights")
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            summary = agent_output.final_answer
            key_points = []
            discussion_highlights = None

        return PostSummary(
            post=post,
            summary=summary,
            key_points=key_points,
            discussion_highlights=discussion_highlights,
        )

    def generate_digest(
        self,
        posts: List[RedditPost],
        subreddit: str,
        start_date: datetime,
        end_date: datetime,
        include_comments: bool = True,
        show_progress: bool = True,
    ) -> SubredditDigest:
        """
        Generate a complete digest for multiple posts with caching support

        Args:
            posts: List of RedditPost objects to summarize
            subreddit: Subreddit name
            start_date: Start date of the digest period
            end_date: End date of the digest period
            include_comments: Whether to include comment analysis
            show_progress: Whether to show progress bar (default: True)

        Returns:
            SubredditDigest with all post summaries
        """
        summaries = []
        total = len(posts)
        cache_hits = 0
        cache_misses = 0

        # Load cache for this subreddit if caching is enabled
        if self.cache:
            self.cache.load(subreddit)

        if not show_progress or not TQDM_AVAILABLE:
            print(f"\nGenerating summaries for {total} posts...")

        # Create progress bar if tqdm is available
        posts_iter = tqdm(
            posts,
            desc="Summarizing posts",
            unit="post",
            total=total,
            disable=not (show_progress and TQDM_AVAILABLE),
        )

        for post in posts_iter:
            try:
                # Update description with current post title
                if show_progress and TQDM_AVAILABLE:
                    posts_iter.set_postfix_str(f"{post.title[:40]}...")

                # Check cache first
                if self.cache:
                    cached = self.cache.get(subreddit, post.post_id)
                    if cached:
                        # Use cached summary
                        summary = PostSummary(
                            post=post,
                            summary=cached["summary"],
                            key_points=cached["key_points"],
                            discussion_highlights=cached["discussion_highlights"],
                        )
                        summaries.append(summary)
                        cache_hits += 1
                        continue

                # Cache miss - generate new summary
                summary = self.summarize_post(post, include_comments=include_comments)
                summaries.append(summary)
                cache_misses += 1

                # Store in cache
                if self.cache:
                    self.cache.put(subreddit, post.post_id, summary)

            except Exception as e:
                if not show_progress or not TQDM_AVAILABLE:
                    print(f"  ⚠️  Error summarizing post '{post.title[:50]}': {e}")
                else:
                    tqdm.write(f"  ⚠️  Error summarizing post '{post.title[:50]}': {e}")
                continue

        # Save cache after processing
        if self.cache:
            self.cache.save(subreddit)
            stats = self.cache.get_stats(subreddit)
            print(f"\n📦 Cache: {stats['hits']} hits, {stats['misses']} misses ({stats['cached_posts']} total cached)")

        digest = SubredditDigest(
            subreddit=subreddit,
            start_date=start_date,
            end_date=end_date,
            post_summaries=summaries,
            total_posts_analyzed=total,
        )

        return digest

    def learn_from_feedback(self, task: str, answer: str, feedback: str) -> None:
        """
        Manual learning: update skillbook based on feedback

        Args:
            task: The original task
            answer: The agent's answer
            feedback: User feedback on the answer quality
        """
        # Use reflector to analyze the performance
        reflection = self.reflector.reflect(
            task=task,
            agent_answer=answer,
            ground_truth=None,
            feedback=feedback,
            skillbook=self.skillbook,
        )

        # Use skill manager to update the skillbook
        updates = self.skill_manager.curate_skills(
            task=task,
            agent_answer=answer,
            reflection=reflection,
            skillbook=self.skillbook,
        )

        # Apply updates to skillbook
        self.skillbook.apply_update(updates)
        print(f"Skillbook updated with {len(updates.operations)} operations")

    def save_skillbook(self, filepath: str) -> None:
        """Save the skillbook to a file"""
        self.skillbook.save_to_file(filepath)
        print(f"Skillbook saved to {filepath}")

    def print_skillbook_stats(self) -> None:
        """Print current skillbook statistics"""
        print(f"\n📊 Skillbook Stats:")
        skills = self.skillbook.skills()  # Call the method to get skills list
        print(f"  Total skills: {len(skills)}")
        for skill in skills:
            print(f"    - {skill.content[:60]}... [+{skill.helpful}/-{skill.harmful}]")
