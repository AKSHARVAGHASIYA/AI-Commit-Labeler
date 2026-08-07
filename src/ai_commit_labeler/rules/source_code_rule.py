from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.rules.base_rule import BaseRule

class SourceCodeRule(BaseRule):
    def match(self, commit: Commit):
        
        files = str(commit.changed_filenames).lower()

        extensions = [
            ".py",
            ".js",
            ".ts",
            ".java",
            ".cpp",
            ".c",
            ".go",
            ".rs",
        ]

        if any(ext in files for ext in extensions):
            return Prediction(
                label="USEFUL",
                confidence=90,
                reason="Source code changes detected.",
            )

        return None