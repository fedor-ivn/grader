from abc import ABC, abstractmethod
from ibash.i_bash import IBash


class Test(ABC):
    @abstractmethod
    def test(self, solution: IBash) -> None:
        ...
