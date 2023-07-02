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

    def test(self, solution: IBashSession) -> bool:
        is_expected = solution.expect_output(
            self._expected_output
        )
        print(self._result.result(is_expected))
        return is_expected

    def score(self, solution: IBashSession) -> int:
        is_expected = solution.expect_output(
            self._expected_output
        )
        return self._result.test_score(is_expected)
