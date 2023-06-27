from tmpgrader.criterion.criterion import Criterion
from tmpgrader.ibash.session import IBashSession


class Criteria:
    def __init__(self, criteria: list[Criterion]):
        self._criteria = criteria

    def test(self, solution: IBashSession):
        return [
            criterion.test(solution)
            for criterion in self._criteria
        ]
