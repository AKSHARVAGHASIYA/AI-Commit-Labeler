from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.rules.base_rule import BaseRule

class ConfigurationRule(BaseRule):
    def match(self, commit: Commit):
        
        files = str(commit.changed_filenames).lower()
        message = commit.commit_message.lower()

        config_files = [
            ".toml",
            ".yaml",
            ".yml",
            ".json",
            ".ini",
            ".cfg",
            ".conf",
            ".env",
            "dockerfile",
            "docker-compose",
            "compose.yml",
        ]

        if (
            any(config in files for config in config_files)
            or "config" in message
            or "configuration" in message
        ):
            return Prediction(
                label="LOW_VALUE",
                confidence=88,
                reason="Configuration changes detected.",
            )

        return None