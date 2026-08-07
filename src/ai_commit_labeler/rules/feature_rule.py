from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.rules.base_rule import BaseRule

class FeatureRule(BaseRule):

    def match(self, commit: Commit):
        message = commit.commit_message.lower()

        keywords = [
            "feat",
            "feature",
            "add",
            "added",
            "implement",
            "implemented",
            "introduce",
            "support",
            "create",
        ]

        if any(word in message for word in keywords):
            return Prediction(
                label="USEFUL",
                confidence=92,
                reason="New feature detected from commit message.",
            )

        return None