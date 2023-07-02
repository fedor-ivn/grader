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

    def test(self, solution: IBashSession) -> bool:
        is_expected = solution.prompt(
            self._expected_prompt, self._enter
        )
        print(self._result.result(is_expected))
        return is_expected

    def score(self, solution: IBashSession) -> int:
        is_expected = solution.prompt(
            self._expected_prompt, self._enter
        )
        return self._result.test_score(is_expected)
