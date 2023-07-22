from grader.criteria.criteria import Criteria
from grader.ibash.session import IBashSession
from grader.criteria.criterion.criterion import Criterion
from grader.output.test_output.test_output import TestOutput


class SequentialCriteria(Criteria):
    """
    This class contains a list of criterias of the task and is used
    to run them and get results
    """

    def __init__(self, criteria: list[Criterion]):
        """
        Initializes a new instance of SequentialCriteria

        Attributes:
            criteria (list[Criterion]): a list of all the criterias in the test
        """
        self._criteria = criteria

    def test(self, solution: IBashSession) -> TestOutput:
        """
        This is used to test every criteria in the list and provide a
        combined output for them

        Args:
            solution (IBashSession): a started bash session
        """
        feedback = ""
        overall_score = 0

        for criterion in self._criteria:
            output = criterion.test(solution)

            feedback += output.feedback()
            feedback += "\n"

            overall_score += output.score()

        return TestOutput(overall_score, feedback)
