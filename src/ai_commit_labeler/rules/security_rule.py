from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.rules.base_rule import BaseRule

class SecurityRule(BaseRule):
    def match(self, commit: Commit):
        
        message = commit.commit_message.lower()
        files = str(commit.changed_filenames).lower()

        security_keywords = [
            "security",
            "vulnerability",
            "cve",
            "auth",
            "authentication",
            "authorization",
            "password",
            "token",
            "jwt",
            "encrypt",
            "encryption",
            "decrypt",
            "csrf",
            "xss",
            "sql injection",
            "permission",
            "oauth",
            "ssl",
            "tls",
        ]

        if (
            any(keyword in message for keyword in security_keywords)
            or any(keyword in files for keyword in security_keywords)
        ):
            return Prediction(
                label="USEFUL",
                confidence=96,
                reason="Security-related changes detected.",
            )

        return None