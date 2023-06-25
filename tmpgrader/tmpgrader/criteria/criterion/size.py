from criterion import Criterion
from ibash.session import IBashSession


class SizeCriterion(Criterion):
    def __init__(self, expected_prompt: str, enter: str):
        pass

    def test(self, solution: IBashSession) -> bool:
        return True
