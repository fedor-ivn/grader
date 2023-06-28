from tmpgrader.criteria.sequential_criteria import (
    SequentialCriteria,
)
from tmpgrader.criteria.criterion.prompt import (
    PromptCriterion,
)
from tmpgrader.criteria.criterion.output import (
    OutputCriterion,
)
from tmpgrader.mock_executable.mock_executable import (
    MockExecutable,
)
from tmpgrader.criteria.criterion.arguments import (
    ArgumentsCriterion,
)
from tmpgrader.ibash.ibash import IBash
from tmpgrader.tests.test import Test


class WalkerTest(Test):
    def __init__(self) -> None:
        self._criteria = SequentialCriteria(
            [
                PromptCriterion(
                    expected_prompt="Какую директорию посмотреть? - ",
                    enter=".",
                ),
                OutputCriterion("asdasd"),
            ]
        )

    def test(self, solution: IBash) -> None:
        self._criteria.test(solution.start_session())
