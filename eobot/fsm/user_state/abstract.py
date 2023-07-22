from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generic, Self, TypeVar

if TYPE_CHECKING:
    from eobot.update.filter.state import OnState

T = TypeVar("T")


class AbstractUserStates(ABC, Generic[T]):
    @abstractmethod
    def state(self, id: int) -> OnState[T]:
        ...

    @abstractmethod
    def match(self, id: int, state: OnState[T]) -> bool:
        ...

    @abstractmethod
    def next(self, id: int) -> Self:
        ...
