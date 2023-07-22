from __future__ import annotations
from typing import TYPE_CHECKING, Self
from eobot.fsm.user_state.abstract import (
    AbstractUserStates,
    T,
)

if TYPE_CHECKING:
    from eobot.update.filter.state import OnState


class DummyUserStates(AbstractUserStates[T]):
    def state(self, _: int) -> OnState[T]:
        return OnState("")

    def match(self, id: int, state: OnState[T]) -> bool:
        return False

    def next(self, _: int) -> Self:
        return self
