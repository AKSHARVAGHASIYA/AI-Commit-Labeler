"""
Base interface for AI providers.
"""

from abc import ABC, abstractmethod

from ai_commit_labeler.models import Commit, Prediction


class AIProvider(ABC):

    @abstractmethod
    def analyze_commit(self, commit: Commit) -> Prediction:
        pass