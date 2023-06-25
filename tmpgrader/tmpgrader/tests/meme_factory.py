from criteria.sequential_criteria import SequentialCriteria
from criteria.criterion.prompt import PromptCriterion
from criteria.criterion.output import OutputCriterion
from mock_executable.mock_executable import MockExecutable
from criteria.criterion.arguments import ArgumentsCriterion
from ibash.ibash import IBash
from tests.test import Test


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
