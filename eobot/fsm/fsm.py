from eobot.tgtypes.message.message import T, Message
from eobot.update.filter.state import OnState
from eobot.update.on_event import OnEvent


class FSM(OnState[T]):
    def __init__(self, states: list[OnState[T]]) -> None:
        self._states = states

    def initial(self) -> OnState[T]:
        return self._states[0]

    def next(self, state: OnState[T]) -> OnState[T]:
        return self._states[
            (self._states.index(state) + 1)
            % len(self._states)
        ]
