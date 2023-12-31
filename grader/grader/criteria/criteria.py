from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession
from grader.output.test_output.test_output import TestOutput


class Criteria:
    def __init__(self, criteria: list[Criterion]):
        self._criteria = criteria

    def test(self, solution: IBashSession) -> TestOutput:
        feedback = ""
        overall_score = 0

        for criterion in self._criteria:
            output = criterion.test(solution)

            feedback += output.feedback()
            feedback += "\n"

            overall_score += output.score()

        return TestOutput(overall_score, feedback)
