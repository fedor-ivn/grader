from grader.criteria.sequential_criteria import (
    SequentialCriteria,
)
from grader.criteria.criterion.prompt import (
    PromptCriterion,
)
from grader.criteria.criterion.output import (
    OutputCriterion,
)
from grader.mock_executable.mock_executable import (
    MockExecutable,
)
from grader.criteria.criterion.arguments import (
    ArgumentsCriterion,
)
from grader.ibash.ibash import IBash
from grader.tests.test import Test
from grader.output.result.result import Result
from grader.output.feedback.feedback import (
    Feedback,
)
from grader.output.score.score import Score

from grader.criteria.criterion.error import (
    ErrorCriterion,
)


class MemeFactoryTest(Test):
    def __init__(self) -> None:
        convert_mock = MockExecutable("convert", "pipes")
        pipe_session = convert_mock.create()
        self._criteria = SequentialCriteria(
            [
                PromptCriterion(
                    expected_prompt="Подпись к мему: ",
                    enter="четыре",
                    result=Result(
                        feedback=Feedback(
                            positive="Скрипт запрашивает подпись для мема",
                            negative="Скрипт не запрашивает подпись для мема",
                        ),
                        score=Score(max_score=5),
                        test_num=1,
                    ),
                ),
                PromptCriterion(
                    expected_prompt="Название файла: ",
                    enter="six-four.jpg",
                    result=Result(
                        feedback=Feedback(
                            positive="Скрипт запрашивает путь выходного файла",
                            negative="Скрипт не запрашивает путь выходного файла",
                        ),
                        score=Score(max_score=5),
                        test_num=2,
                    ),
                ),
                ArgumentsCriterion(
                    convert_mock,
                    result=Result(
                        feedback=Feedback(
                            positive="Скрипт создаёт мем согласно заданным параметрам",
                            negative="Скрипт не создаёт мем согласно заданным параметрам",
                        ),
                        score=Score(max_score=55),
                        test_num=3,
                    ),
                ),
                OutputCriterion(
                    "Мем сохранён!\r\n",
                    result=Result(
                        feedback=Feedback(
                            positive="Скрипт выводит сообщение, что мем сохранён",
                            negative="Скрипт не выводит сообщение, что мем сохранён",
                        ),
                        score=Score(max_score=5),
                        test_num=4,
                    ),
                ),
                ErrorCriterion(
                    result=Result(
                        feedback=Feedback(
                            positive="Скрипт выполняется без ошибок",
                            negative="Скрипт выполняется с ошибками",
                        ),
                        score=Score(max_score=30),
                        test_num=5,
                    ),
                ),
            ]
        )

    def test(self, solution: IBash) -> str:
        return f"{self._criteria.feedback()}"

    def test_score(self, solution: IBash) -> str:
        return f"Overall score: {self._criteria.score()}"

    def output(self, file: str) -> str:
        self._criteria.test(IBash(file).start_session())
        return f"Test results:\n{self.test(IBash(file))}\n{self.test_score(IBash(file))}"
    

print(MemeFactoryTest().output("solution.sh"))


