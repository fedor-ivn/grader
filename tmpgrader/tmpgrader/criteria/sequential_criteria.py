from tmpgrader.criterion.criterion import Criterion
from tmpgrader.ibash.session import IBashSession


class SequentialCriteria(Criterion):
    def __init__(self, criteria: list[Criterion]):
        self._criteria = criteria

    def test(self, solution: IBashSession):
        for criterion in self._criteria:
            result = criterion.test(solution)
            if not result:
                return False
        return True
