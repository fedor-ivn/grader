from criteria.sequential_criteria import SequentialCriteria
from criteria.criterion.prompt import PromptCriterion
from criteria.criterion.output import OutputCriterion
from mock_executable.mock_executable import MockExecutable
from criteria.criterion.arguments import ArgumentsCriterion
from ibash.ibash import IBash
from tests.test import Test


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
