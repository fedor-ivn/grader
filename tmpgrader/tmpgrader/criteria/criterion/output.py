from tmpgrader.criterion import Criterion
from tmpgrader.ibash.session import IBashSession


class OutputCriterion(Criterion):
    def __init__(self, expected_output: str):
        self._expected_output = expected_output

    def test(self, solution: IBashSession):
        is_expected = solution.expect_output(
            self._expected_output
        )
        print(is_expected)
        return is_expected
