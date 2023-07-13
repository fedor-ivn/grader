from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession

from grader.ibash.session import IBashSession
from grader.output.result.result import Result

from grader.criteria.criterion.criterion_output.criterion_output import CriterionOutput


class ErrorCriterion(Criterion):
    """
    The class implementing an error test. Needed to check if the script returned an error or not
    """

    def __init__(self, result: Result) -> None:
        """
        Initializes a new ErrorCriterion instance

        Attributes:
            result (Result): results of the test
        """
        self._result = result
        self._is_expected = False

    def test(self, solution: IBashSession) -> CriterionOutput:
        """
        Runs a test of the function and returns the output

        Args:
            solution (IBashSession): a started bash session
        """
        return_code = solution.check_error()

        is_expected = False

        if return_code == 0:
            is_expected = True

        return CriterionOutput(
            is_passed=is_expected,
            feedback=self._result.result(is_expected),
            score=self._result.test_score(is_expected),
        )
