from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.rules.base_rule import BaseRule

class DependencyRule(BaseRule):
        def match(self, commit: Commit):
            message = commit.commit_message.lower()
            files = str(commit.changed_filenames).lower()

            if (
                "dependabot" in message
                or "bump" in message
                or "requirements" in files
                or "package.json" in files
                or "poetry.lock" in files
            ):
                return Prediction(
                    label="LOW_VALUE",
                    confidence=92,
                    reason="Dependency update detected.",
                )

            return None