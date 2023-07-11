from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession
from grader.output.result.result import Result

from grader.criteria.criterion.criterion_output.criterion_output import CriterionOutput


class SizeCriterion(Criterion):
    """
    Criterion checking the size of the solution
    """
    def __init__(
        self, max_size: int, result: Result
    ) -> None:
        self._max_size = max_size
        self._result = result

    def test(self, solution: IBashSession) -> CriterionOutput:
        return CriterionOutput(
            is_passed=True,
            feedback=self._result.result(True),
            score=self._result.test_score(True),
        )
