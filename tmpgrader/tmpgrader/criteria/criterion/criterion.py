from abc import ABC, abstractmethod


class Criterion(ABC):
    @abstractmethod
    def test(self, solution: str) -> bool:
        pass
