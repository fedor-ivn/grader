from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar("T")


class UpdateFactory(ABC, Generic[T]):
    @abstractmethod
    def construct_update(self, update_id: int) -> T:
        ...
