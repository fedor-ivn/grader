from __future__ import annotations
from typing import TYPE_CHECKING, Self
from vedis import Vedis

from eobot.fsm.user_state.abstract import (
    AbstractUserStates,
    T,
)

if TYPE_CHECKING:
    from eobot.fsm.fsm import FSM

from eobot.update.filter.state import OnState


class UserStates(AbstractUserStates[T]):
    def __init__(self, fsm: FSM[T], db: Vedis) -> None:
        self._fsm = fsm
        self._db = db

    def state(self, id: int) -> OnState[T]:
        try:
            return OnState(self._db.get(id).decode())
        except KeyError:
            initial = self._fsm.initial()
            self._db.set(id, initial.name)
            return initial

    def match(self, id: int, state: OnState[T]) -> bool:
        return self.state(id) == state

    def next(self, id: int) -> Self:
        self._db.set(
            id, self._fsm.next(self.state(id)).name
        )
        return self
