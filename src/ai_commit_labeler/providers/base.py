"""
Base interface for AI providers.
"""

from abc import ABC, abstractmethod


class AIProvider(ABC):
    """
    Base class for all AI providers.
    """

    @abstractmethod
    def analyze_commit(self, commit):
        """
        Analyze a commit and return a prediction.
        """
        raise NotImplementedError