"""
Rule-based AI provider.
"""

from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.providers.base import AIProvider


class RuleProvider(AIProvider):
    """
    Heuristic-based provider for commit classification.
    """

    def analyze_commit(self, commit: Commit) -> Prediction:

        rules = [
            self._documentation_rule,
            self._dependency_rule,
            self._test_rule,
            self._source_code_rule,
        ]

        for rule in rules:
            prediction = rule(commit)
            if prediction:
                return prediction

        return Prediction(
            label="UNCERTAIN",
            confidence=60,
            reason="No matching rule found.",
        )

    def _documentation_rule(self, commit: Commit):
        files = str(commit.changed_filenames).lower()

        if (
            "readme" in files
            or ".md" in files
            or "docs" in files
        ):
            return Prediction(
                label="LOW_VALUE",
                confidence=95,
                reason="Documentation-only changes detected.",
            )

        return None

    def _dependency_rule(self, commit: Commit):
        message = commit.commit_message.lower()
        files = str(commit.changed_filenames).lower()

        if (
            "dependabot" in message
            or "bump" in message
            or "requirements" in files
            or "package.json" in files
            or "poetry.lock" in files
        ):
            return Prediction(
                label="LOW_VALUE",
                confidence=92,
                reason="Dependency update detected.",
            )

        return None

    def _test_rule(self, commit: Commit):
        files = str(commit.changed_filenames).lower()

        if (
            "test" in files
            or "tests" in files
        ):
            return Prediction(
                label="USEFUL",
                confidence=88,
                reason="Test files were modified.",
            )

        return None

    def _source_code_rule(self, commit: Commit):
        files = str(commit.changed_filenames).lower()

        extensions = [
            ".py",
            ".js",
            ".ts",
            ".java",
            ".cpp",
            ".c",
            ".go",
            ".rs",
        ]

        if any(ext in files for ext in extensions):
            return Prediction(
                label="USEFUL",
                confidence=90,
                reason="Source code changes detected.",
            )

        return None