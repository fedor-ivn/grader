from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession
from grader.mock_executable.mock_executable import (
    MockExecutable,
)
from grader.output.result.result import Result

from grader.criteria.criterion.criterion_output.criterion_output import CriterionOutput


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
        self._is_expected = False

    def test(self, solution: IBashSession) -> CriterionOutput:
        collected_args = self._pipe_session.collect_args()

        success = True

        if collected_args[0] != "-gravity":
            success = False

        if collected_args[1] not in ["south", "north"]:
            success = False

        if collected_args[2] != "-annotate":
            success = False

        if collected_args[3] != "0":
            success = False

        if collected_args[4] != "четыре":
            success = False

        if collected_args[5] != "six-four.jpg":
            success = False

        self._is_expected = success

        return CriterionOutput(
            is_passed=success,
            feedback=self._result.result(success),
            score=self._result.test_score(success),
        )
