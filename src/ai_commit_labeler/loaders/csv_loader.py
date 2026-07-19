"""
CSV loader for GitHub commits.
"""

from pathlib import Path

import pandas as pd

from ai_commit_labeler.models import Commit


class CSVLoader:
    """Loads GitHub commits from a CSV file."""

    REQUIRED_COLUMNS = (
        "repository",
        "sha",
        "commit_message",
        "changed_filenames",
        "file_summary",
        "patch_summary",
    )

    @staticmethod
    def _clean(value) -> str:
        """
        Convert missing values to an empty string.
        """

        if pd.isna(value):
            return ""

        return str(value).strip()

    def load(self, csv_path: str | Path) -> list[Commit]:
        """
        Load commits from a CSV file.
        """

        csv_path = Path(csv_path)

        if not csv_path.exists():
            raise FileNotFoundError(f"File not found: {csv_path}")

        df = pd.read_csv(csv_path)

        missing_columns = [
            column
            for column in self.REQUIRED_COLUMNS
            if column not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                "Missing required columns: "
                + ", ".join(missing_columns)
            )

        commits: list[Commit] = []

        for row in df.itertuples(index=False):

            commits.append(
                Commit(
                    repository=self._clean(row.repository),
                    sha=self._clean(row.sha),
                    commit_message=self._clean(row.commit_message),
                    changed_filenames=self._clean(row.changed_filenames),
                    file_summary=self._clean(row.file_summary),
                    patch_summary=self._clean(row.patch_summary),
                )
            )

        return commits