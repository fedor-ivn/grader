from grader.criteria.criteria import Criteria
from grader.ibash.session import IBashSession
from grader.criteria.criterion.criterion import Criterion


class SequentialCriteria(Criteria):
    def __init__(self, criteria: list[Criterion]):
        self._criteria = criteria

    def test(self, solution: IBashSession) -> None:
        for criterion in self._criteria:
            criterion.test(solution)
    
    def feedback(self) -> str:
        result = ""
        for criterion in self._criteria:
            result += criterion.feedback()
            result += "\n"
        return result

    def score(self) -> int:
        overall_score = 0
        for criterion in self._criteria:
            overall_score += criterion.score()
        return overall_score
