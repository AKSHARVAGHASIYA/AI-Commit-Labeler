"""
Rule-based AI provider.
"""

from ai_commit_labeler.models import Commit, Prediction
from ai_commit_labeler.providers.base import AIProvider


class RuleProvider(AIProvider):
    """
    Heuristic-based provider for commit classification.
    """

    def analyze_commit(self, commit: Commit) -> Prediction:

        rules = [
            self._documentation_rule,
            self._dependency_rule,
            self._bugfix_rule,
            self._feature_rule,
            self._refactor_rule,
            self._ci_rule,
            self._configuration_rule,
            self._security_rule,
            self._test_rule,
            self._source_code_rule,
        ]

        for rule in rules:
            prediction = rule(commit)
            if prediction:
                return prediction

        return Prediction(
            label="UNCERTAIN",
            confidence=60,
            reason="No matching rule found.",
        )

    def _documentation_rule(self, commit: Commit):
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

    def _dependency_rule(self, commit: Commit):
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
    
    def _bugfix_rule(self, commit: Commit):

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

    def _feature_rule(self, commit: Commit):

        message = commit.commit_message.lower()

        keywords = [
            "feat",
            "feature",
            "add",
            "added",
            "implement",
            "implemented",
            "introduce",
            "support",
            "create",
        ]

        if any(word in message for word in keywords):
            return Prediction(
                label="USEFUL",
                confidence=92,
                reason="New feature detected from commit message.",
            )

        return None
    
    def _refactor_rule(self, commit: Commit):

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
    
    def _ci_rule(self, commit: Commit):

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
    
    def _configuration_rule(self, commit: Commit):

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
    
    def _security_rule(self, commit: Commit):

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

    def _test_rule(self, commit: Commit):
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

    def _source_code_rule(self, commit: Commit):
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