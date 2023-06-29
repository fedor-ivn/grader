from tmpgrader.criterion import Criterion
from tmpgrader.ibash.session import IBashSession


class PromptCriterion(Criterion):
    def __init__(self, expected_prompt: str, enter: str):
        self._expected_prompt = expected_prompt
        self._enter = enter

    def test(self, solution: IBashSession):
        is_expected = solution.prompt(
            self._expected_prompt, self._enter
        )
        print(is_expected)
        return is_expected
