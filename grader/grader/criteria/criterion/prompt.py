from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession
from grader.output.result.result import Result

from grader.criteria.criterion.criterion_output.criterion_output import CriterionOutput


class PromptCriterion(Criterion):
    def __init__(
        self,
        expected_prompt: str,
        enter: str,
        result: Result,
    ) -> None:
        self._expected_prompt = expected_prompt
        self._enter = enter
        self._result = result

    def test(self, solution: IBashSession) -> CriterionOutput:
        is_expected = solution.prompt(self._expected_prompt, self._enter)
        return CriterionOutput(
            is_passed=is_expected,
            feedback=self._result.result(is_expected),
            score=self._result.test_score(is_expected),
        )
