from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.rules.base_rule import BaseRule


class ReleaseRule(BaseRule):

    def match(self, commit: Commit):

        message = commit.commit_message.lower()

        keywords = [
            "release",
            "version",
            "bump version",
            "tag",
            "changelog",
            "prepare release",
            "publish",
        ]

        if any(keyword in message for keyword in keywords):
            return Prediction(
                label="LOW_VALUE",
                confidence=90,
                reason="Release/version related changes detected.",
            )

        return None