from typing import Self
from vedis import Vedis

from eobot.fsm.fsm import FSM


class UserStates:
    def __init__(self, fsm: FSM, db: Vedis) -> None:
        self._fsm = fsm
        self._db = db

    def state(self, id: int) -> str:
        try:
            return self._db.get(id).decode()  # type: ignore
        except KeyError:
            initial = self._fsm.initial()
            self._db.set(id, initial)
            return initial

    def match(self, id: int, state: str) -> bool:
        return self.state(id) == state

    def next(self, id: int) -> Self:
        self._db.set(id, self._fsm.next(self.state(id)))
        return self
