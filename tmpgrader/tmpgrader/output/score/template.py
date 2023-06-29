from abc import ABC


class ScoreTemplate(ABC):
    def __init__(self, max_score: int) -> None:
        self.max_score = max_score

    def score(self, is_passed: bool) -> int:
        if is_passed:
            return self.max_score
        return 0