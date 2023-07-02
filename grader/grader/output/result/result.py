from abc import ABC
from grader.output.score.score import (
    Score,
)
from grader.output.feedback.feedback import (
    Feedback,
)


class Result(ABC):
    def __init__(
        self,
        test_num: int,
        score: Score,
        feedback: Feedback,
    ) -> None:
        self.score = score
        self.feedback = feedback
        self.test_num = test_num

    def result(self, is_passed: bool) -> str:
        return f"{self.test_num}. Score: {self.score.score(is_passed)}, Feedback: {self.feedback.feedback(is_passed)}"

    def test_score(self, is_passed: bool) -> int:
        return self.score.score(is_passed)
