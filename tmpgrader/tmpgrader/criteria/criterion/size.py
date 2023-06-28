from tmpgrader.riterion import Criterion
from tmpgrader.ibash.session import IBashSession


class SizeCriterion(Criterion):
    def __init__(self, expected_prompt: str, enter: str):
        pass

    def test(self, solution: IBashSession) -> bool:
        return True
