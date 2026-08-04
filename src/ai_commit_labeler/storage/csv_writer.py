"""
CSV writer for review results.
"""

from pathlib import Path
import csv

from ai_commit_labeler.models import Commit, Prediction


class CSVWriter:

    HEADER = [
        "repository",
        "sha",
        "ai_label",
        "final_label",
        "confidence",
        "decision",
    ]

    def __init__(self, output_file: str = "review_results.csv"):
        self.output_file = Path(output_file)

        if not self.output_file.exists():
            with open(self.output_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def save(
        self,
        commit: Commit,
        prediction: Prediction,
        final_label: str,
        decision: str,
    ):

        with open(self.output_file, "a", newline="") as f:

            writer = csv.writer(f)

            writer.writerow(
                [
                    commit.repository,
                    commit.sha,
                    prediction.label,
                    final_label,
                    prediction.confidence,
                    decision,
                ]
            )