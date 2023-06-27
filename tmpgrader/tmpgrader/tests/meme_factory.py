from tmpgrader.criteria.sequential_criteria import SequentialCriteria
from tmpgrader.criteria.criterion.prompt import PromptCriterion
from tmpgrader.criteria.criterion.output import OutputCriterion
from tmpgrader.mock_executable.mock_executable import MockExecutable
from tmpgrader.criteria.criterion.arguments import ArgumentsCriterion
from tmpgrader.ibash.ibash import IBash
from tmpgrader.tests.test import Test


class MemeFactoryTest(Test):
    def __init__(self) -> None:
        convert_mock = MockExecutable("convert", "pipes")
        pipe_session = convert_mock.create()
        self._criteria = SequentialCriteria(
            [
                SequentialCriteria(
                    [
                        PromptCriterion(
                            expected_prompt="Подпись к мему: ",
                            enter="четыре",
                        ),
                        PromptCriterion(
                            expected_prompt="Название файла: ",
                            enter="six-four.jpg",
                        ),
                    ]
                ),
                SequentialCriteria(
                    [
                        ArgumentsCriterion(convert_mock),
                    ]
                ),
                OutputCriterion("Мем сохранён!\r\n"),
            ]
        )

    def test(self, solution: IBash) -> None:
        self._criteria.test(solution.start_session())
