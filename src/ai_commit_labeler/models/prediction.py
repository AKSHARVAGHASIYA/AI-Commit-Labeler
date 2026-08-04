"""
Prediction data model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Prediction:
    """
    AI prediction for a commit.
    """

    label: str
    confidence: int
    reason: str