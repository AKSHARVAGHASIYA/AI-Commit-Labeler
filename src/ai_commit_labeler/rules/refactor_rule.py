from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.rules.base_rule import BaseRule

class RefactorRule(BaseRule):

    def match(self, commit: Commit):
        message = commit.commit_message.lower()

        keywords = [
            "refactor",
            "cleanup",
            "clean up",
            "rename",
            "restructure",
            "reorganize",
            "simplify",
            "improve code",
            "code cleanup",
        ]

        if any(keyword in message for keyword in keywords):
            return Prediction(
                label="USEFUL",
                confidence=85,
                reason="Refactoring or code cleanup detected.",
            )

        return None