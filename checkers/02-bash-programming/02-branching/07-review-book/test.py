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

HELP = "Доступные команды:\r\n\r\n\
  help         - вывести справку по командам\r\n\
  add-review   - добавить отзыв\r\n\
  list-reviews - показать все отзывы\r\n\
  clear        - удалить все отзывы\r\n> "


criteria = SequentialCriteria(
    [
        PromptCriterion(
            expected_prompt="> ",
            enter="help",
            result=Result(
                feedback=Feedback(
                    positive="Код запускается корректно",
                    negative="Код запускается некорректно",
                ),
                score=Score(max_score=1),
                test_num=1,
            ),
        ),
        OutputCriterion(
            expected_output=HELP,
            result=Result(
                feedback=Feedback(
                    positive="Команда help работает корректно",
                    negative="Команда help работает некорректно",
                ),
                score=Score(max_score=24),
                test_num=2,
            ),
        ),
        PromptCriterion(
            expected_prompt="",
            enter="add-review",
            result=Result(
                feedback=Feedback(
                    positive="Скрипт запрашивает следующую команду",
                    negative="Скрипт не запрашивает следующую команду",
                ),
                score=Score(max_score=1),
                test_num=3,
            ),
        ),
        PromptCriterion(
            expected_prompt="Введите свой отзыв: ",
            enter="Пицца «Четыре сыра» очень вкусная! Теперь за пиццей буду ходить только к вам!",
            result=Result(
                feedback=Feedback(
                    positive="Команда add-review запрашивает отзыв",
                    negative="Команда add-review не запрашивает отзыв",
                ),
                score=Score(max_score=9),
                test_num=4,
            ),
        ),
        PromptCriterion(
            expected_prompt="Спасибо за ваш отзыв!\r\n> ",
            enter="list-reviews",
            result=Result(
                feedback=Feedback(
                    positive="Команда add-review получает отзыв",
                    negative="Команда add-review не получает отзыв",
                ),
                score=Score(max_score=15),
                test_num=5,
            ),
        ),
        PromptCriterion(
            expected_prompt="-----\r\n\
Пицца «Четыре сыра» очень вкусная! Теперь за пиццей буду ходить только к вам!\r\n\
-----\r\n> ",
            enter="clear",
            result=Result(
                feedback=Feedback(
                    positive="Команда list-reviews выводит отзывы",
                    negative="Команда list-reviews не выводит отзывы",
                ),
                score=Score(max_score=20),
                test_num=6,
            ),
        ),
        PromptCriterion(
            expected_prompt="Все отзывы удалены\r\n> ",
            enter="list-reviews",
            result=Result(
                feedback=Feedback(
                    positive="Команда clear выполняется",
                    negative="Команда clear не выполняется",
                ),
                score=Score(max_score=10),
                test_num=7,
            ),
        ),
        PromptCriterion(
            expected_prompt="Отзывов ещё нет :(\r\n> ",
            enter="blah-blah",
            result=Result(
                feedback=Feedback(
                    positive="Команда clear удаляет отзывы",
                    negative="Команда clear не удаляет отзывы",
                ),
                score=Score(max_score=15),
                test_num=8,
            ),
        ),
        OutputCriterion(
            expected_output="Неизвестная команда. Введите help, чтобы узнать о доступных командах\r\n> ",
            result=Result(
                feedback=Feedback(
                    positive="Неизвестная команда обрабатывается корректно",
                    negative="Неизвестная команда обрабатывается некорректно",
                ),
                score=Score(max_score=5),
                test_num=9,
            ),
        ),
    ]
)


# with open("reference-solution.sh") as file:
#     print(Test().output(IBash(file.read())))
