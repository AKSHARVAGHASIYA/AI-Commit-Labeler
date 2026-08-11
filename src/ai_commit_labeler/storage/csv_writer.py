import csv
from pathlib import Path


class CSVWriter:

    def __init__(self, output_file="review_results.csv"):
        self.output_file = Path(output_file)

        if not self.output_file.exists():
            with open(self.output_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "repository",
                    "sha",
                    "commit_message",
                    "ai_label",
                    "ai_confidence",
                    "final_label",
                    "action",
                ])

    def save(self, commit, prediction, final_label, decision):

        with open(self.output_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow([
                commit.repository,
                commit.sha,
                commit.commit_message,
                prediction.label,
                prediction.confidence,
                final_label,
                decision,
            ])