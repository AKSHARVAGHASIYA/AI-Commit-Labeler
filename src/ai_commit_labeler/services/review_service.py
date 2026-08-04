"""
Review service for AI Commit Labeler.
"""

from pathlib import Path

from ai_commit_labeler.loaders import CSVLoader
from ai_commit_labeler.models import Commit
from ai_commit_labeler.providers import MockProvider


class ReviewService:
    """
    Coordinates the review workflow.
    """

    def __init__(self) -> None:
        self.loader = CSVLoader()
        self.provider = MockProvider()

    def load_commits(self, csv_path: str | Path) -> list[Commit]:
        return self.loader.load(csv_path)

    def review_commit(self, commit: Commit):
        """
        Analyze a single commit.
        """

        prediction = self.provider.analyze_commit(commit)

        return prediction