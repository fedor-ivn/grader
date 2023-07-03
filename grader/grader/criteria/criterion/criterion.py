from abc import ABC, abstractmethod

from grader.ibash.session import IBashSession
from grader.output.result.result import Result


class Criterion(ABC):
    @abstractmethod
    def test(self, solution: IBashSession) -> bool:
        ...

    @abstractmethod
    def feedback(self) -> str:
        ...

    @abstractmethod
    def score(self) -> int:
        ...
