"""
Review service for AI Commit Labeler.
"""

from pathlib import Path

from ai_commit_labeler.loaders import CSVLoader
from ai_commit_labeler.models import Commit
from ai_commit_labeler.providers import RuleProvider


class ReviewService:
    """
    Coordinates the review workflow.
    """

    def __init__(self) -> None:
        self.loader = CSVLoader()
        self.provider = RuleProvider()

    def load_commits(self, csv_path: str | Path) -> list[Commit]:
        return self.loader.load(csv_path)

    def review_commit(self, commit: Commit):
        """
        Analyze a single commit.
        """

        prediction = self.provider.analyze_commit(commit)

        return prediction
    
    def get_reviewed_shas(self, output_file="review_results.csv"):
        import csv
        from pathlib import Path

        reviewed = set()

        file_path = Path(output_file)

        if not file_path.exists():
            return reviewed

        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                reviewed.add(row["sha"])

        return reviewed