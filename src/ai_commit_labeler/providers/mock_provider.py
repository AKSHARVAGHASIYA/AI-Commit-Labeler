"""
Mock AI provider.
"""

from ai_commit_labeler.providers.base import AIProvider


class MockProvider(AIProvider):
    """
    Fake AI provider used during development.
    """

    def analyze_commit(self, commit):
        return {
            "label": "LOW_VALUE",
            "confidence": 95,
            "reason": "Mock prediction for development."
        }