"""
Mock AI provider.
"""

from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.providers.base import AIProvider


class MockProvider(AIProvider):

    def analyze_commit(self, commit: Commit) -> Prediction:

        return Prediction(
            label="LOW_VALUE",
            confidence=95,
            reason="Documentation-only changes detected.",
        )