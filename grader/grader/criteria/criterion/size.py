from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession
from grader.output.result.result import Result

from grader.criteria.criterion.criterion_output.criterion_output import (
    CriterionOutput,
)


class SizeCriterion(Criterion):
    """
    Criterion checking the size of the solution
    """

    def __init__(
        self, max_size: int, result: Result
    ) -> None:
        """
        Initializes a new ArgumentsCriterion instance

        Attributes:
            max_size (int): the maximum size of the script
            result (Result): results of the test
        """
        self._max_size = max_size
        self._result = result

    def test(
        self, solution: IBashSession
    ) -> CriterionOutput:
        """
        Runs a test of the function and returns the output

        Args:
            solution (IBashSession): a started bash session
        """
        return CriterionOutput(
            is_passed=True,
            feedback=self._result.result(True),
            score=self._result.test_score(True),
        )
