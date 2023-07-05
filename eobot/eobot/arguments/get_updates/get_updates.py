from eobot.arguments.argument import (
    MethodArgument,
)
from eobot.arguments.get_updates.allowed_updates import (
    AbstractAllowedUpdates,
    DefaultAllowedUpdates,
)
from eobot.arguments.method_arguments import (
    MethodArguments,
)
from eobot.arguments.inline import InlineArgument
from typing import Any

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class GetUpdatesArguments(MethodArgument):
    def __init__(
        self,
        offset: int = -1,
        limit: int = 100,
        timeout: int = 0,
        allowed_updates: AbstractAllowedUpdates = DefaultAllowedUpdates(),
        log: AbstractLog = NoLog(),
    ) -> None:
        self._offset = offset
        self._limit = limit
        self._timeout = timeout
        self._allowed_updates = allowed_updates
        self._log = log

    def with_offset(
        self, offset: int
    ) -> "GetUpdatesArguments":
        self._log.debug(f"Setting offset to {offset}")
        return GetUpdatesArguments(
            offset,
            self._limit,
            self._timeout,
            self._allowed_updates,
        )

    def to_dict(self) -> dict[str, Any]:
        self._log.debug(
            "Converting GetUpdatesArguments to dict"
        )
        return MethodArguments(
            [
                InlineArgument("offset", self._offset),
                InlineArgument("limit", self._limit),
                InlineArgument("timeout", self._timeout),
                self._allowed_updates,
            ]
        ).to_dict()
