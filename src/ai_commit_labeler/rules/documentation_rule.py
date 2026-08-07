from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.rules.base_rule import BaseRule


class DocumentationRule(BaseRule):

    def match(self, commit: Commit):

        files = str(commit.changed_filenames).lower()

        if (
            "readme" in files
            or ".md" in files
            or "docs" in files
        ):
            return Prediction(
                label="LOW_VALUE",
                confidence=95,
                reason="Documentation-only changes detected.",
            )

        return None