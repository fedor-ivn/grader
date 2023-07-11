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
from grader.tests.test import TestTemplate
from grader.output.result.result import Result
from grader.output.feedback.feedback import (
    Feedback,
)
from grader.output.score.score import Score

from grader.criteria.criterion.error import (
    ErrorCriterion,
)
from grader.output.test_output.test_output import TestOutput

HELP = '''Доступные команды:

  help         - вывести справку по командам
  add-review   - добавить отзыв
  list-reviews - показать все отзывы
  clear        - удалить все отзывы'''


class Test(TestTemplate):
    def __init__(self) -> None:
        convert_mock = MockExecutable("convert", "/tmp")
        pipe_session = convert_mock.create()
        self._criteria = SequentialCriteria(
            [
                PromptCriterion(
                    expected_prompt=HELP,
                    enter="help",
                    result=Result(
                        feedback=Feedback(
                            positive="Команда help работает корректно",
                            negative="Команда help работает некорректно",
                        ),
                        score=Score(max_score=25),
                        test_num=1,
                    ),
                ),
                PromptCriterion(
                    expected_prompt="Введите свой отзыв: ",
                    enter="add-review",
                    result=Result(
                        feedback=Feedback(
                            positive="Команда add-review запрашивает отзыв",
                            negative="Команда add-review не запрашивает отзыв",
                        ),
                        score=Score(max_score=10),
                        test_num=2,
                    ),
                ),
                PromptCriterion(
                    expected_prompt="Спасибо за ваш отзыв!",
                    enter="Пицца «Четыре сыра» очень вкусная! Теперь за пиццей буду ходить только к вам!",
                    result=Result(
                        feedback=Feedback(
                            positive="Команда add-review получает отзыв",
                            negative="Команда add-review не получает отзыв",
                        ),
                        score=Score(max_score=15),
                        test_num=3,
                    ),
                ),
                PromptCriterion(
                    expected_prompt="""-----
Пицца «Четыре сыра» очень вкусная! Теперь за пиццей буду ходить только к вам!
-----""",
                    enter="list-reviews",
                    result=Result(
                        feedback=Feedback(
                            positive="Команда list-reviews выводит отзывы",
                            negative="Команда list-reviews не выводит отзывы",
                        ),
                        score=Score(max_score=25),
                        test_num=4,
                    ),
                ),
                PromptCriterion(
                    expected_prompt="Все отзывы удалены",
                    enter="clear",
                    result=Result(
                        feedback=Feedback(
                            positive="Команда clear выполняется",
                            negative="Команда clear не выполняется",
                        ),
                        score=Score(max_score=10),
                        test_num=5,
                    ),
                ),
                PromptCriterion(
                    expected_prompt="Отзывов ещё нет :(",
                    enter="list-reviews",
                    result=Result(
                        feedback=Feedback(
                            positive="Команда clear удаляет отзывы",
                            negative="Команда clear не удаляет отзывы",
                        ),
                        score=Score(max_score=10),
                        test_num=6,
                    ),
                ),
                PromptCriterion(
                    expected_prompt="Неизвестная команда. Введите help, чтобы узнать о доступных командах",
                    enter="blah-blah",
                    result=Result(
                        feedback=Feedback(
                            positive="Неизвестная команда обрабатывается корректно",
                            negative="Неизвестная команда обрабатывается некорректно",
                        ),
                        score=Score(max_score=5),
                        test_num=7,
                    ),
                ),
            ]
        )

    def output(self, solution: IBash) -> str:
        test_output: TestOutput
        test_output = self._criteria.test(
            solution.start_session()
        )
        return test_output.output()  # type: ignore


print(Test().output(IBash("reference-solution.sh")))
