from abc import ABC, abstractmethod
from grader.ibash.ibash import IBash


class TestTemplate(ABC):
    @abstractmethod
    def test(self, solution: IBash) -> None:
        ...
