"""
Tests for RedditSummarizer with ACE framework integration
"""

import json
import os
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

import pytest

# Mock praw and ACE modules before importing summarizer
sys.modules['praw'] = Mock()
sys.modules['praw.exceptions'] = Mock()
sys.modules['prawcore'] = Mock()
sys.modules['prawcore.exceptions'] = Mock()

from reddit_summarizer.models import RedditPost, PostSummary, SubredditDigest
from reddit_summarizer.summarizer import RedditSummarizer


@pytest.fixture
def mock_llm_client():
    """Fixture for mocked LLM client"""
    with patch("reddit_summarizer.summarizer.LiteLLMClient") as mock:
        client = Mock()
        mock.return_value = client
        yield client


@pytest.fixture
def mock_agent():
    """Fixture for mocked Agent"""
    with patch("reddit_summarizer.summarizer.Agent") as mock:
        agent = Mock()
        mock.return_value = agent
        yield agent


@pytest.fixture
def mock_fetcher():
    """Fixture for mocked RedditFetcher"""
    fetcher = Mock()
    fetcher.fetch_post_comments.return_value = [
        {"author": "commenter1", "body": "Great post!", "score": 10},
        {"author": "commenter2", "body": "I agree with this.", "score": 5},
    ]
    return fetcher


class TestRedditSummarizer:
    """Test cases for RedditSummarizer class"""

    def test_initialization_new_skillbook(self, mock_llm_client):
        """Test initializing summarizer with new skillbook"""
        summarizer = RedditSummarizer(model="gpt-4o-mini")

        assert summarizer.model == "gpt-4o-mini"
        assert summarizer.skillbook is not None
        assert (
            summarizer.skillbook.title == "Reddit Post Summarization"
        )
        assert summarizer.agent is not None
        assert summarizer.reflector is not None
        assert summarizer.skill_manager is not None

    def test_initialization_with_existing_skillbook(
        self, mock_llm_client, tmp_path
    ):
        """Test loading existing skillbook"""
        # Create a temporary skillbook file
        skillbook_path = tmp_path / "test_skillbook.json"
        skillbook_data = {
            "title": "Test Skillbook",
            "objective": "Test objective",
            "skills": [],
        }
        with open(skillbook_path, "w") as f:
            json.dump(skillbook_data, f)

        with patch(
            "reddit_summarizer.summarizer.Skillbook.load_from_file"
        ) as mock_load:
            mock_skillbook = Mock()
            mock_skillbook.title = "Test Skillbook"
            mock_load.return_value = mock_skillbook

            summarizer = RedditSummarizer(
                model="gpt-4o-mini",
                skillbook_path=str(skillbook_path),
            )

            mock_load.assert_called_once_with(str(skillbook_path))
            assert summarizer.skillbook == mock_skillbook

    def test_summarize_post_without_comments(
        self, mock_llm_client, sample_post
    ):
        """Test summarizing a post without fetching comments"""
        summarizer = RedditSummarizer(model="gpt-4o-mini")

        # Mock agent response
        mock_output = Mock()
        mock_output.final_answer = json.dumps({
            "summary": "This is a test summary.",
            "key_points": ["Point 1", "Point 2", "Point 3"],
            "discussion_highlights": "Active discussion.",
        })
        summarizer.agent.generate_answer = Mock(return_value=mock_output)

        summary = summarizer.summarize_post(sample_post, include_comments=False)

        assert isinstance(summary, PostSummary)
        assert summary.post == sample_post
        assert summary.summary == "This is a test summary."
        assert len(summary.key_points) == 3
        assert summary.discussion_highlights == "Active discussion."

    def test_summarize_post_with_comments(
        self, mock_llm_client, sample_post, mock_fetcher
    ):
        """Test summarizing a post with comments"""
        summarizer = RedditSummarizer(
            model="gpt-4o-mini",
            fetcher=mock_fetcher,
        )

        # Mock agent response
        mock_output = Mock()
        mock_output.final_answer = json.dumps({
            "summary": "Summary with comments.",
            "key_points": ["Point A", "Point B"],
            "discussion_highlights": "Great discussion.",
        })
        summarizer.agent.generate_answer = Mock(return_value=mock_output)

        summary = summarizer.summarize_post(sample_post, include_comments=True)

        # Verify fetcher was called
        mock_fetcher.fetch_post_comments.assert_called_once()

        assert isinstance(summary, PostSummary)
        assert summary.summary == "Summary with comments."
        assert len(summary.key_points) == 2

    def test_summarize_post_json_parse_fallback(
        self, mock_llm_client, sample_post
    ):
        """Test fallback when JSON parsing fails"""
        summarizer = RedditSummarizer(model="gpt-4o-mini")

        # Mock agent response with invalid JSON
        mock_output = Mock()
        mock_output.final_answer = "This is plain text, not JSON"
        summarizer.agent.generate_answer = Mock(return_value=mock_output)

        summary = summarizer.summarize_post(sample_post, include_comments=False)

        assert isinstance(summary, PostSummary)
        assert summary.summary == "This is plain text, not JSON"
        assert summary.key_points == []
        assert summary.discussion_highlights is None

    def test_generate_digest(
        self, mock_llm_client, sample_post_list
    ):
        """Test generating a complete digest"""
        summarizer = RedditSummarizer(model="gpt-4o-mini")

        # Mock agent to return valid summaries
        mock_output = Mock()
        mock_output.final_answer = json.dumps({
            "summary": "Test summary",
            "key_points": ["Point 1"],
            "discussion_highlights": None,
        })
        summarizer.agent.generate_answer = Mock(return_value=mock_output)

        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 1, 31)

        digest = summarizer.generate_digest(
            posts=sample_post_list,
            subreddit="test",
            start_date=start_date,
            end_date=end_date,
            include_comments=False,
            show_progress=False,
        )

        assert isinstance(digest, SubredditDigest)
        assert digest.subreddit == "test"
        assert digest.start_date == start_date
        assert digest.end_date == end_date
        assert len(digest.post_summaries) == 5
        assert digest.total_posts_analyzed == 5

    def test_generate_digest_with_checkpoint(
        self, mock_llm_client, sample_post_list, tmp_path
    ):
        """Test digest generation with checkpoint saving"""
        summarizer = RedditSummarizer(model="gpt-4o-mini")

        # Mock agent response
        mock_output = Mock()
        mock_output.final_answer = json.dumps({
            "summary": "Test",
            "key_points": ["P1"],
            "discussion_highlights": None,
        })
        summarizer.agent.generate_answer = Mock(return_value=mock_output)

        checkpoint_file = tmp_path / "checkpoint.json"
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 1, 31)

        digest = summarizer.generate_digest(
            posts=sample_post_list,
            subreddit="test",
            start_date=start_date,
            end_date=end_date,
            include_comments=False,
            show_progress=False,
            checkpoint_file=str(checkpoint_file),
            checkpoint_interval=2,
        )

        assert isinstance(digest, SubredditDigest)
        # Checkpoint file should be deleted after successful completion
        assert not checkpoint_file.exists()

    def test_checkpoint_save_and_load(
        self, mock_llm_client, sample_post_list, tmp_path
    ):
        """Test checkpoint save and resume functionality"""
        summarizer = RedditSummarizer(model="gpt-4o-mini")
        checkpoint_file = tmp_path / "checkpoint.json"

        # Create a mock summary
        summary = PostSummary(
            post=sample_post_list[0],
            summary="Test summary",
            key_points=["Point 1"],
            discussion_highlights=None,
        )

        # Save checkpoint
        summarizer._save_checkpoint(
            str(checkpoint_file),
            [summary],
            1,
        )

        assert checkpoint_file.exists()

        # Load checkpoint
        summaries, next_index = summarizer._load_checkpoint(
            str(checkpoint_file)
        )

        assert len(summaries) == 1
        assert next_index == 1
        assert summaries[0].summary == "Test summary"
        assert summaries[0].post.title == sample_post_list[0].title

    def test_learn_from_feedback(self, mock_llm_client):
        """Test manual learning from feedback"""
        summarizer = RedditSummarizer(model="gpt-4o-mini")

        # Mock reflector and skill manager
        mock_reflection = Mock()
        summarizer.reflector.reflect = Mock(return_value=mock_reflection)

        mock_updates = Mock()
        mock_updates.operations = [Mock(), Mock()]
        summarizer.skill_manager.curate_skills = Mock(
            return_value=mock_updates
        )

        summarizer.skillbook.apply_updates = Mock()

        # Call learn_from_feedback
        summarizer.learn_from_feedback(
            task="Test task",
            answer="Test answer",
            feedback="Good summary but could be more concise",
        )

        # Verify methods were called
        summarizer.reflector.reflect.assert_called_once()
        summarizer.skill_manager.curate_skills.assert_called_once()
        summarizer.skillbook.apply_updates.assert_called_once_with(mock_updates)

    def test_save_skillbook(self, mock_llm_client, tmp_path):
        """Test saving skillbook to file"""
        summarizer = RedditSummarizer(model="gpt-4o-mini")
        skillbook_path = tmp_path / "saved_skillbook.json"

        summarizer.skillbook.save_to_file = Mock()

        summarizer.save_skillbook(str(skillbook_path))

        summarizer.skillbook.save_to_file.assert_called_once_with(
            str(skillbook_path)
        )

    def test_print_skillbook_stats(self, mock_llm_client, capsys):
        """Test printing skillbook statistics"""
        summarizer = RedditSummarizer(model="gpt-4o-mini")

        # Mock skillbook with some skills
        mock_skill = Mock()
        mock_skill.content = "Test skill content for testing purposes and more"
        mock_skill.helpful = 5
        mock_skill.harmful = 2
        summarizer.skillbook.skills = [mock_skill]

        summarizer.print_skillbook_stats()

        captured = capsys.readouterr()
        assert "Skillbook Stats" in captured.out
        assert "Reddit Post Summarization" in captured.out
        assert "Total skills: 1" in captured.out

    def test_generate_digest_error_handling(
        self, mock_llm_client, sample_post_list
    ):
        """Test digest generation continues on individual post errors"""
        summarizer = RedditSummarizer(model="gpt-4o-mini")

        # Mock agent to fail on first post, succeed on others
        call_count = [0]

        def mock_generate_answer(*args, **kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                raise Exception("Test error")
            mock_output = Mock()
            mock_output.final_answer = json.dumps({
                "summary": "Success",
                "key_points": ["P1"],
                "discussion_highlights": None,
            })
            return mock_output

        summarizer.agent.generate_answer = Mock(
            side_effect=mock_generate_answer
        )

        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 1, 31)

        digest = summarizer.generate_digest(
            posts=sample_post_list,
            subreddit="test",
            start_date=start_date,
            end_date=end_date,
            include_comments=False,
            show_progress=False,
        )

        # Should have 4 summaries (1 failed, 4 succeeded)
        assert len(digest.post_summaries) == 4
        assert digest.total_posts_analyzed == 5
