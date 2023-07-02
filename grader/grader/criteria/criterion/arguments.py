from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession
from grader.mock_executable.mock_executable import (
    MockExecutable,
)
from grader.output.result.result import Result


class ArgumentsCriterion(Criterion):
    def __init__(
        self,
        mock_executable: MockExecutable,
        result: Result,
    ):
        self._mock_executable = mock_executable
        # todo: govnokod
        self._pipe_session = self._mock_executable.create()
        self._pipe_session.start_session()
        self._result = result

    def test(self, solution: IBashSession) -> bool:
        collected_args = self._pipe_session.collect_args()
        print(collected_args)
        print(self._result.result(True))
        return True

    def score(self, solution: IBashSession) -> int:
        return self._result.test_score(True)
