from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession

from grader.ibash.session import IBashSession
from grader.output.result.result import Result


class ErrorCriterion(Criterion):
    def __init__(
        self, result: Result
    ) -> None:
        self._result = result
        self._is_expected = False

    def test(self, solution: IBashSession) -> bool: 
        return_code = solution.check_error()
        if return_code == 0:
            self._is_expected = True
        else:
            self._is_expected = False
        return self._is_expected

    def feedback(self) -> str:
        return self._result.result(self._is_expected)

    def score(self) -> int:
        return self._result.test_score(self._is_expected)
