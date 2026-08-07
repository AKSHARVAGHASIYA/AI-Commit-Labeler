from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.rules.base_rule import BaseRule


class PerformanceRule(BaseRule):

    def match(self, commit: Commit):

        message = commit.commit_message.lower()

        keywords = [
            "optimize",
            "optimization",
            "performance",
            "improve performance",
            "speed",
            "faster",
            "slow",
            "latency",
            "throughput",
            "cache",
            "caching",
            "memory",
            "reduce memory",
            "efficient",
        ]

        if any(keyword in message for keyword in keywords):
            return Prediction(
                label="USEFUL",
                confidence=93,
                reason="Performance improvements detected.",
            )

        return None