from tmpgrader.criteria.criterion.criterion import Criterion
from tmpgrader.ibash.session import IBashSession
from tmpgrader.mock_executable.mock_executable import (
    MockExecutable,
)


class ArgumentsCriterion(Criterion):
    def __init__(self, mock_executable: MockExecutable):
        self._mock_executable = mock_executable
        # todo: govnokod
        self._pipe_session = self._mock_executable.create()
        self._pipe_session.start_session()

    def test(self, solution: IBashSession) -> bool:
        collected_args = self._pipe_session.collect_args()
        print(collected_args)
        return True
