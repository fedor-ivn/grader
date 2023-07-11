from abc import ABC, abstractmethod

from grader.ibash.session import IBashSession
from grader.output.result.result import Result

from grader.criteria.criterion.criterion_output.criterion_output import CriterionOutput


class Criterion(ABC):
    @abstractmethod
    def test(self, solution: IBashSession) -> CriterionOutput:
        ...
