from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.rules.base_rule import BaseRule

class CiRule(BaseRule):
    def match(self, commit: Commit):
        message = commit.commit_message.lower()
        files = str(commit.changed_filenames).lower()

        keywords = [
            "workflow",
            "github actions",
            "ci",
            "jenkins",
            "travis",
            "circleci",
            "azure pipeline",
            "pipeline",
        ]

        if (
            any(keyword in message for keyword in keywords)
            or ".github/workflows" in files
            or ".github" in files
        ):
            return Prediction(
                label="LOW_VALUE",
                confidence=90,
                reason="CI/CD configuration changes detected.",
            )

        return None