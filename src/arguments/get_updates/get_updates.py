from arguments.argument import (
    MethodArgument,
)
from arguments.get_updates.allowed_updates import (
    AbstractAllowedUpdates,
    PreviousAllowedUpdates,
)
from arguments.method_arguments import (
    MethodArguments,
)
from arguments.inline import InlineArgument
from typing import Any


class GetUpdatesArguments(MethodArgument):
    def __init__(
        self,
        offset: int = -1,
        limit: int = 100,
        timeout: int = 0,
        allowed_updates: AbstractAllowedUpdates = PreviousAllowedUpdates(),
    ) -> None:
        self._offset = offset
        self._limit = limit
        self._timeout = timeout
        self._allowed_updates = allowed_updates

    def with_offset(
        self, offset: int
    ) -> "GetUpdatesArguments":
        return GetUpdatesArguments(
            offset,
            self._limit,
            self._timeout,
            self._allowed_updates,
        )

    def to_dict(self) -> dict[str, Any]:
        return MethodArguments(
            [
                InlineArgument("offset", self._offset),
                InlineArgument("limit", self._limit),
                InlineArgument("timeout", self._timeout),
                self._allowed_updates,
            ]
        ).to_dict()
