from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession

from grader.ibash.session import IBashSession
from grader.output.result.result import Result

from grader.criteria.criterion.criterion_output.criterion_output import CriterionOutput


class SingleEchoCriterion(Criterion):
    """
    The class which checks what the script writes to stdout
    """

    def __init__(self, expected_output: str, result: Result) -> None:
        """
        Initializes a new ArgumentsCriterion instance

        Attributes:
            expected_output (str): an output that we expect to receive from the script
            result (Result): results of the test
        """

        self._expected_output = expected_output
        self._result = result

    def test(self, solution: IBashSession) -> CriterionOutput:
        """
        Runs a test of the function and returns the output

        Args:
            solution (IBashSession): a started bash session
        """
        is_expected = solution.expect_single_output(self._expected_output)
        return CriterionOutput(
            is_passed=is_expected,
            feedback=self._result.result(is_expected),
            score=self._result.test_score(is_expected),
        )
