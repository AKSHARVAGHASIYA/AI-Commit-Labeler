"""
Review service for AI Commit Labeler.
"""

from pathlib import Path

from ai_commit_labeler.loaders import CSVLoader
from ai_commit_labeler.models import Commit


class ReviewService:
    """
    Coordinates the commit review workflow.
    """

    def __init__(self) -> None:
        self.loader = CSVLoader()

    def load_commits(self, csv_path: str | Path) -> list[Commit]:
        """
        Load commits from a CSV file.
        """

        return self.loader.load(csv_path)