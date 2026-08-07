from ai_commit_labeler.providers.base import AIProvider
from ai_commit_labeler.models import Prediction

from ai_commit_labeler.rules.documentation_rule import DocumentationRule
from ai_commit_labeler.rules.dependency_rule import DependencyRule
from ai_commit_labeler.rules.bugfix_rule import BugfixRule
from ai_commit_labeler.rules.feature_rule import FeatureRule
from ai_commit_labeler.rules.refactor_rule import RefactorRule
from ai_commit_labeler.rules.ci_rule import CiRule
from ai_commit_labeler.rules.configuration_rule import ConfigurationRule
from ai_commit_labeler.rules.security_rule import SecurityRule
from ai_commit_labeler.rules.test_rule import TestRule
from ai_commit_labeler.rules.source_code_rule import SourceCodeRule


class RuleProvider(AIProvider):

    def __init__(self):
        self.rules = [
            DocumentationRule(),
            DependencyRule(),
            BugfixRule(),
            FeatureRule(),
            RefactorRule(),
            CiRule(),
            ConfigurationRule(),
            SecurityRule(),
            TestRule(),
            SourceCodeRule(),
        ]

    def analyze_commit(self, commit):

        for rule in self.rules:
            prediction = rule.match(commit)
            if prediction:
                return prediction

        return Prediction(
            label="UNCERTAIN",
            confidence=60,
            reason="No matching rule found.",
        )