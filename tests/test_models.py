"""Unit tests for Reddit Summarizer data models"""

import pytest
from datetime import datetime
from reddit_summarizer.models import RedditPost, PostSummary, SubredditDigest


class TestRedditPost:
    """Tests for RedditPost model"""

    def test_post_creation(self, sample_post):
        """Test creating a RedditPost instance"""
        assert sample_post.title == "Sample Post Title"
        assert sample_post.author == "test_user"
        assert sample_post.score == 250
        assert sample_post.num_comments == 75

    def test_full_url_property(self, sample_post):
        """Test full_url property generates correct URL"""
        expected_url = "https://reddit.com/r/test/comments/abc123/sample_post_title/"
        assert sample_post.full_url == expected_url

    def test_meets_threshold_default(self, sample_post):
        """Test meets_threshold with default values (100 upvotes, 30 comments)"""
        assert sample_post.meets_threshold() is True

    def test_meets_threshold_custom(self, sample_post):
        """Test meets_threshold with custom values"""
        assert sample_post.meets_threshold(min_upvotes=200, min_comments=50) is True
        assert sample_post.meets_threshold(min_upvotes=300, min_comments=50) is False
        assert sample_post.meets_threshold(min_upvotes=200, min_comments=100) is False

    def test_meets_threshold_edge_cases(self, sample_post):
        """Test meets_threshold edge cases"""
        # Exact match should pass
        assert sample_post.meets_threshold(min_upvotes=250, min_comments=75) is True
        # One below should fail
        assert sample_post.meets_threshold(min_upvotes=251, min_comments=75) is False
        assert sample_post.meets_threshold(min_upvotes=250, min_comments=76) is False

    def test_to_dict(self, sample_post):
        """Test to_dict conversion"""
        post_dict = sample_post.to_dict()

        assert post_dict["title"] == "Sample Post Title"
        assert post_dict["author"] == "test_user"
        assert post_dict["upvotes"] == 250
        assert post_dict["comments"] == 75
        assert post_dict["url"] == "https://reddit.com/r/test/comments/abc123/sample_post_title/"
        assert post_dict["date"] == "2024-01-15"

    def test_to_dict_truncates_long_content(self):
        """Test that to_dict truncates long post content"""
        long_content = "x" * 2000
        post = RedditPost(
            title="Test",
            author="user",
            url="https://reddit.com/test",
            selftext=long_content,
            score=100,
            num_comments=30,
            created_utc=datetime.now(),
            permalink="/r/test/comments/123/test/",
            post_id="123",
            subreddit="test",
        )

        post_dict = post.to_dict()
        assert len(post_dict["content"]) <= 1000

    def test_to_dict_link_post(self):
        """Test to_dict for link posts (no selftext)"""
        post = RedditPost(
            title="Link Post",
            author="user",
            url="https://example.com",
            selftext="",
            score=100,
            num_comments=30,
            created_utc=datetime.now(),
            permalink="/r/test/comments/123/link_post/",
            post_id="123",
            subreddit="test",
        )

        post_dict = post.to_dict()
        assert post_dict["content"] == "[Link Post]"


class TestPostSummary:
    """Tests for PostSummary model"""

    def test_summary_creation(self, sample_summary):
        """Test creating a PostSummary instance"""
        assert sample_summary.summary == "This is a concise summary of the post."
        assert len(sample_summary.key_points) == 3
        assert sample_summary.discussion_highlights is not None

    def test_to_markdown_basic(self, sample_summary):
        """Test basic markdown generation"""
        markdown = sample_summary.to_markdown()

        # Check header
        assert "### [Sample Post Title]" in markdown
        assert "https://reddit.com" in markdown

        # Check metadata
        assert "**Author:** u/test_user" in markdown
        assert "**Upvotes:** 250" in markdown
        assert "**Comments:** 75" in markdown
        assert "**Date:** 2024-01-15" in markdown

        # Check summary
        assert "**Summary:** This is a concise summary" in markdown

        # Check key points
        assert "**Key Points:**" in markdown
        assert "- Point 1" in markdown
        assert "- Point 2" in markdown
        assert "- Point 3" in markdown

        # Check discussion highlights
        assert "**Discussion Highlights:**" in markdown
        assert "Active discussion about testing strategies" in markdown

    def test_to_markdown_without_discussion(self, sample_post):
        """Test markdown generation without discussion highlights"""
        summary = PostSummary(
            post=sample_post,
            summary="Summary without discussion",
            key_points=["Point 1"],
            discussion_highlights=None,
        )

        markdown = summary.to_markdown()
        assert "**Discussion Highlights:**" not in markdown

    def test_to_markdown_ends_with_separator(self, sample_summary):
        """Test that markdown ends with separator"""
        markdown = sample_summary.to_markdown()
        assert markdown.strip().endswith("---")


class TestSubredditDigest:
    """Tests for SubredditDigest model"""

    def test_digest_creation(self, sample_post_list, sample_summary):
        """Test creating a SubredditDigest instance"""
        digest = SubredditDigest(
            subreddit="test",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31),
            post_summaries=[sample_summary],
            total_posts_analyzed=10,
        )

        assert digest.subreddit == "test"
        assert len(digest.post_summaries) == 1
        assert digest.total_posts_analyzed == 10

    def test_to_markdown_structure(self, sample_summary):
        """Test overall markdown structure"""
        digest = SubredditDigest(
            subreddit="python",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31),
            post_summaries=[sample_summary],
            total_posts_analyzed=15,
        )

        markdown = digest.to_markdown()

        # Check title
        assert "# r/python Reading Digest" in markdown

        # Check metadata
        assert "**Period:** 2024-01-01 to 2024-01-31" in markdown
        assert "**Posts Summarized:** 1" in markdown
        assert "**Total Posts Analyzed:** 15" in markdown

        # Check separator
        assert "---" in markdown

        # Check post numbering
        assert "## 1." in markdown

    def test_to_markdown_multiple_posts(self, sample_post_list):
        """Test markdown with multiple posts"""
        summaries = []
        for post in sample_post_list[:3]:
            summary = PostSummary(
                post=post, summary=f"Summary for {post.title}", key_points=["Point"]
            )
            summaries.append(summary)

        digest = SubredditDigest(
            subreddit="test",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31),
            post_summaries=summaries,
            total_posts_analyzed=10,
        )

        markdown = digest.to_markdown()

        # Check all posts are numbered
        assert "## 1." in markdown
        assert "## 2." in markdown
        assert "## 3." in markdown

        # Check counts
        assert "**Posts Summarized:** 3" in markdown

    def test_save_to_file(self, sample_summary, tmp_path):
        """Test saving digest to file"""
        digest = SubredditDigest(
            subreddit="test",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31),
            post_summaries=[sample_summary],
            total_posts_analyzed=5,
        )

        # Use pytest's tmp_path fixture
        output_file = tmp_path / "test_digest.md"
        digest.save_to_file(str(output_file))

        # Verify file was created
        assert output_file.exists()

        # Verify content
        content = output_file.read_text(encoding="utf-8")
        assert "# r/test Reading Digest" in content
        assert "Sample Post Title" in content

    def test_empty_digest(self):
        """Test digest with no summaries"""
        digest = SubredditDigest(
            subreddit="test",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31),
            post_summaries=[],
            total_posts_analyzed=0,
        )

        markdown = digest.to_markdown()
        assert "**Posts Summarized:** 0" in markdown
        assert "**Total Posts Analyzed:** 0" in markdown

    def test_to_json(self, sample_summary):
        """Test JSON conversion"""
        digest = SubredditDigest(
            subreddit="test",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31),
            post_summaries=[sample_summary],
            total_posts_analyzed=5,
        )

        json_data = digest.to_json()

        # Check structure
        assert json_data["subreddit"] == "test"
        assert json_data["start_date"] == "2024-01-01"
        assert json_data["end_date"] == "2024-01-31"
        assert json_data["total_posts_analyzed"] == 5
        assert json_data["posts_summarized"] == 1

        # Check summaries
        assert len(json_data["summaries"]) == 1
        summary = json_data["summaries"][0]
        assert summary["title"] == "Sample Post Title"
        assert summary["upvotes"] == 250
        assert summary["comments"] == 75
        assert summary["summary"] == "This is a concise summary of the post."
        assert len(summary["key_points"]) == 3

    def test_save_to_json_file(self, sample_summary, tmp_path):
        """Test saving digest to JSON file"""
        import json

        digest = SubredditDigest(
            subreddit="test",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31),
            post_summaries=[sample_summary],
            total_posts_analyzed=5,
        )

        # Save as JSON
        output_file = tmp_path / "test_digest.json"
        digest.save_to_file(str(output_file))

        # Verify file was created
        assert output_file.exists()

        # Verify content is valid JSON
        with open(output_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data["subreddit"] == "test"
        assert len(data["summaries"]) == 1

    def test_save_auto_detects_format(self, sample_summary, tmp_path):
        """Test that save_to_file auto-detects format by extension"""
        digest = SubredditDigest(
            subreddit="test",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31),
            post_summaries=[sample_summary],
            total_posts_analyzed=5,
        )

        # Save as markdown
        md_file = tmp_path / "digest.md"
        digest.save_to_file(str(md_file))
        assert md_file.exists()
        md_content = md_file.read_text(encoding="utf-8")
        assert md_content.startswith("# r/test Reading Digest")

        # Save as JSON
        json_file = tmp_path / "digest.json"
        digest.save_to_file(str(json_file))
        assert json_file.exists()
        json_content = json_file.read_text(encoding="utf-8")
        assert json_content.startswith("{")
