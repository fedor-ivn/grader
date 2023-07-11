from grader.criteria.criteria import Criteria
from grader.ibash.session import IBashSession
from grader.criteria.criterion.criterion import Criterion
from grader.output.test_output.test_output import TestOutput


class SequentialCriteria(Criteria):
    def __init__(self, criteria: list[Criterion]):
        self._criteria = criteria

    def test(self, solution: IBashSession) -> TestOutput:
        feedback = ""
        overall_score = 0
        for criterion in self._criteria:
            criterion.test(solution)
            feedback += criterion.feedback()
            feedback += "\n"
            overall_score += criterion.score()
        return TestOutput(overall_score, feedback)
