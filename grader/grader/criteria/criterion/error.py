from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession

from grader.ibash.session import IBashSession
from grader.output.result.result import Result

from grader.criteria.criterion.criterion_output.criterion_output import CriterionOutput


class ErrorCriterion(Criterion):
    def __init__(self, result: Result) -> None:
        """
        The class implementing an error test. Needed to check if the script returned an error or not 
        """
        self._result = result
        self._is_expected = False

    def test(self, solution: IBashSession) -> CriterionOutput:
        return_code = solution.check_error()

        is_expected = False

        if return_code == 0:
            is_expected = True

        return CriterionOutput(
            is_passed=is_expected,
            feedback=self._result.result(is_expected),
            score=self._result.test_score(is_expected),
        )
