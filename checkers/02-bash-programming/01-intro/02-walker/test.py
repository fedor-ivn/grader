from grader.criteria.sequential_criteria import (
    SequentialCriteria,
)
from grader.criteria.criterion.prompt import (
    PromptCriterion,
)
from grader.criteria.criterion.output import (
    OutputCriterion,
)
from grader.output.result.result import Result
from grader.output.feedback.feedback import (
    Feedback,
)
from grader.output.score.score import Score

from grader.criteria.criterion.error import (
    ErrorCriterion,
)

from grader.criteria.criterion.size import (
    SizeCriterion,
)

from grader.output.test_output.test_output import TestOutput

import os


criteria = SequentialCriteria(
    [
        PromptCriterion(
            expected_prompt="Какую директорию посмотреть? - ",
            enter=".",
            result=Result(
                feedback=Feedback(
                    positive="Скрипт запрашивает путь до директории",
                    negative="Скрипт не запрашивает путь до директории",
                ),
                score=Score(max_score=15),
                test_num=1,
            ),
        ),
        OutputCriterion(
            "__pycache__  reference-solution.sh  test.py\r\n",
            result=Result(
                feedback=Feedback(
                    positive="Скрипт показывает содержимое указанной директории",
                    negative="Скрипт не показывает содержимое указанной директории",
                ),
                score=Score(max_score=25),
                test_num=2,
            ),
        ),
        PromptCriterion(
            expected_prompt="Какую директорию посмотреть? - ",
            enter=".",
            result=Result(
                feedback=Feedback(
                    positive="Скрипт не изменяет рабочую директорию",
                    negative="Скрипт изменяет рабочую директорию",
                ),
                score=Score(max_score=10),
                test_num=3,
            ),
        ),
        OutputCriterion(
            "__pycache__  reference-solution.sh  test.py\r\n",
            result=Result(
                feedback=Feedback(
                    positive="Скрипт работает бесконечно",
                    negative="Скрипт работает не бесконечно",
                ),
                score=Score(max_score=25),
                test_num=4,
            ),
        ),
        SizeCriterion(
            max_size=140,
            size=os.path.getsize("reference-solution.sh"),
            result=Result(
                feedback=Feedback(
                    positive="Скрипт не превышает максимальный размер",
                    negative="Скрипт превышает максимальный размер",
                ),
                score=Score(max_score=25),
                test_num=5,
            ),
        ),
    ]
)


# with open("reference-solution.sh") as file:
#     print(Test().output(IBash(file.read())))
