from abc import ABC, abstractmethod

from grader.ibash.session import IBashSession
from grader.output.result.result import Result


class Criterion(ABC):
    @abstractmethod
    def test(self, solution: IBashSession) -> bool:
        pass

    @abstractmethod
    def score(self, solution: IBashSession) -> int:
        pass
