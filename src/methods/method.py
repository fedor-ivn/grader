from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Method(ABC, Generic[T]):
    @abstractmethod
    def call(self) -> T:
        pass
