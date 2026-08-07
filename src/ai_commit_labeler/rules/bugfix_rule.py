from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.rules.base_rule import BaseRule

class BugfixRule(BaseRule):
    def match(self, commit: Commit):
        
        message = commit.commit_message.lower()

        keywords = [
            "fix",
            "fixed",
            "bug",
            "issue",
            "resolve",
            "resolved",
            "patch",
            "correct",
            "repair",
            "hotfix",
        ]

        if any(word in message for word in keywords):
            return Prediction(
                label="USEFUL",
                confidence=94,
                reason="Bug fix detected from commit message.",
            )

        return None