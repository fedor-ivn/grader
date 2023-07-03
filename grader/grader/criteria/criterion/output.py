from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession

from grader.ibash.session import IBashSession
from grader.output.result.result import Result


class OutputCriterion(Criterion):
    def __init__(
        self, expected_output: str, result: Result
    ) -> None:
        self._expected_output = expected_output
        self._result = result
        self._is_expected = False

    def test(self, solution: IBashSession) -> bool:
        self._is_expected = solution.expect_output(
            self._expected_output
        )
        return self._is_expected

    def feedback(self) -> str:
        return self._result.result(self._is_expected)

    def score(self) -> int:
        return self._result.test_score(self._is_expected)
