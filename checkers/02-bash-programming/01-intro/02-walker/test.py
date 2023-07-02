from grader.criteria.sequential_criteria import (
    SequentialCriteria,
)
from grader.criteria.criterion.prompt import (
    PromptCriterion,
)
from grader.criteria.criterion.output import (
    OutputCriterion,
)

from grader.ibash.ibash import IBash
from grader.tests.test import Test


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


WalkerTest().test(IBash("reference-solution.sh"))
