from grader.criteria.sequential_criteria import (
    SequentialCriteria,
)
from grader.ibash.ibash import IBash
from grader.output.result.result import Result
from grader.output.feedback.feedback import (
    Feedback,
)
from grader.output.score.score import Score

from grader.criteria.criterion.error import (
    ErrorCriterion,
)
from grader.criteria.criterion.output import (
    OutputCriterion,
)


criteria = SequentialCriteria(
    [
        OutputCriterion(
            expected_output="\\ [] _ () /\r\n",
            result=Result(
                feedback=Feedback(
                    positive="Строка выводится верно",
                    negative="Строка выводится неверно",
                ),
                score=Score(max_score=70),
                test_num=1,
            ),
        ),
        ErrorCriterion(
            result=Result(
                feedback=Feedback(
                    positive="Скрипт выполняется без ошибок",
                    negative="Скрипт выполняется с ошибками",
                ),
                score=Score(max_score=30),
                test_num=2,
            ),
        ),
    ]
)

# print(
#     Test(criteria).output(
#         IBash('echo "\\ [] _ () /"')
#     )
# )
