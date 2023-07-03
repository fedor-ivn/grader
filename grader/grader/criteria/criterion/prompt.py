from grader.criteria.criterion.criterion import Criterion
from grader.ibash.session import IBashSession
from grader.output.result.result import Result


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
        self._is_expected = False

    def test(self, solution: IBashSession) -> bool:
        self._is_expected = solution.prompt(
            self._expected_prompt, self._enter
        )
        return self._is_expected

    def feedback(self) -> str:
        return self._result.result(self._is_expected)

    def score(self) -> int:
        return self._result.test_score(self._is_expected)
