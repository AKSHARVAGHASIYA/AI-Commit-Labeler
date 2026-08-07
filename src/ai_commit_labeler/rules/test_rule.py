from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.rules.base_rule import BaseRule

class TestRule(BaseRule):
    def match(self, commit: Commit):
        
        files = str(commit.changed_filenames).lower()

        if (
            "test" in files
            or "tests" in files
        ):
            return Prediction(
                label="USEFUL",
                confidence=88,
                reason="Test files were modified.",
            )

        return None