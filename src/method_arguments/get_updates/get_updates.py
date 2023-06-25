from method_arguments.method_argument import (
    AbstractMethodArgument,
)
from method_arguments.empty import EmptyArgument
from method_arguments.method_arguments import (
    MethodArguments,
)
from method_arguments.inline import InlineMethodArgument
from typing import Any


class GetUpdatesArguments(AbstractMethodArgument):
    def __init__(
        self,
        offset: int = 0,
        limit: int = 100,
        timeout: int = 0,
        allowed_updates: AbstractMethodArgument = EmptyArgument(),
    ) -> None:
        self._offset = offset
        self._limit = limit
        self._timeout = timeout
        self._allowed_updates = allowed_updates

    def to_dict(self) -> dict[str, Any]:
        return MethodArguments(
            [
                InlineMethodArgument(
                    "offset", self._offset
                ),
                InlineMethodArgument("limit", self._limit),
                InlineMethodArgument(
                    "timeout", self._timeout
                ),
                self._allowed_updates,
            ]
        ).to_dict()
