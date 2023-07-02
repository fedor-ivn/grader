from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession
from grader.output.result.result import Result


class SizeCriterion(Criterion):
    def __init__(
        self, max_size: int, result: Result
    ) -> None:
        self._max_size = max_size
        self._result = result

    def test(self, solution: IBashSession) -> bool:
        return True

    def score(self) -> int:
        return self._result.test_score()
