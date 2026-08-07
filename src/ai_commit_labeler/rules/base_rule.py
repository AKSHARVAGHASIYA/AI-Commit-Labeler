from ai_commit_labeler.models import Commit, Prediction


class BaseRule:
    def match(self, commit: Commit) -> Prediction | None:
        raise NotImplementedError