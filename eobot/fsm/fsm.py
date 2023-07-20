class FSM:
    def __init__(self, states: list[str]) -> None:
        self._states = states

    def initial(self) -> str:
        return self._states[0]

    def next(self, state: str) -> str:
        return self._states[
            (self._states.index(state) + 1)
            % len(self._states)
        ]
