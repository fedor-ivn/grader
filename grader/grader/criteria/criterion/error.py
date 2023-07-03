from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession

from grader.ibash.session import IBashSession
from grader.output.result.result import Result


class ErrorCriterion(Criterion):
    def __init__(
        self, result: Result
    ) -> None:
        self._result = result

    def test(self, solution: IBashSession) -> bool: 
        return_code = solution.check_error()
        if return_code == 0:
            print(self._result.result(True))
            return True
        print(self._result.result(False))
        return False

    def score(self, solution: IBashSession) -> int:
        return_code = solution.check_error()
        if return_code == 0:
            success = True
        else: 
            success = False
        return self._result.test_score(success)
