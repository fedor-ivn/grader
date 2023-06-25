from typing import Any
from arguments.argument import MethodArgument


class MergedArgument(MethodArgument):
    def __init__(
        self,
        initial: MethodArgument,
        update: MethodArgument,
    ) -> None:
        self._initial = initial
        self._update = update

    def to_dict(self) -> dict[str, Any]:
        return (
            self._initial.to_dict() | self._update.to_dict()
        )
