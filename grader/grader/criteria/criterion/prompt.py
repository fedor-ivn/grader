from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession
from grader.output.result.result import Result

from grader.criteria.criterion.criterion_output.criterion_output import CriterionOutput


class PromptCriterion(Criterion):
    """
    The criterion to write something to stdin and wait for a specific output
    """

    def __init__(
        self,
        expected_prompt: str,
        enter: str,
        result: Result,
    ) -> None:
        """
        Initializes a new ArgumentsCriterion instance

        Attributes:
            expected_prompt (str): an output that we expect to receive from the script
            enter (str): the string that we are entering into stdin
            result (Result): results of the test
        """
        self._expected_prompt = expected_prompt
        self._enter = enter
        self._result = result

    def test(self, solution: IBashSession) -> CriterionOutput:
        """
        Runs a test of the function and returns the output

        Args:
            solution (IBashSession): a started bash session
        """
        is_expected = solution.prompt(self._expected_prompt, self._enter)
        return CriterionOutput(
            is_passed=is_expected,
            feedback=self._result.result(is_expected),
            score=self._result.test_score(is_expected),
        )
