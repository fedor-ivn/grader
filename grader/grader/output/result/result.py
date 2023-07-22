from abc import ABC
from grader.output.score.score import (
    Score,
)
from grader.output.feedback.feedback import (
    Feedback,
)


class Result(ABC):
    """
    The class containing the whole result of the criteria
    """

    def __init__(
        self,
        test_num: int,
        score: Score,
        feedback: Feedback,
    ) -> None:
        """
        Creates a new Result instance.

        Attributes:
            score (Score): score for the solution.
            feedback (Feedback): feedback for the solution.
            test_num (int): the chronological number of the criteria.
        """
        self.score = score
        self.feedback = feedback
        self.test_num = test_num

    def result(self, is_passed: bool) -> str:
        """
        Returns the string - result of the criterion.

        Args:
            is_passed (bool): Whether the criterion was passed or not.
        """
        return f"{self.test_num}. Score: {self.score.score(is_passed)}, Feedback: {self.feedback.feedback(is_passed)}"

    def test_score(self, is_passed: bool) -> int:
        """
        Returns the points for the criterion.

        Args:
            is_passed (bool): Whether the criterion was passed or not.
        """
        return self.score.score(is_passed)
