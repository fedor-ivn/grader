from arguments.argument import (
    MethodArgument,
)
from arguments.inline import InlineArgument
from typing import Any

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class AbstractAllowedUpdates(MethodArgument):
    pass


class DefaultAllowedUpdates(AbstractAllowedUpdates):
    def to_dict(self) -> dict[str, Any]:
        return InlineArgument(
            "allowed_updates", []
        ).to_dict()


class AllowedUpdates(AbstractAllowedUpdates):
    def __init__(
        self,
        message: bool = True,
        edited_channel_post: bool = True,
        callback_query: bool = True,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._message = message
        self._edited_channel_post = edited_channel_post
        self._callback_query = callback_query
        self.log = log

    def to_dict(self) -> dict[str, Any]:
        self.log.debug("AllowedUpdates.to_dict()")
        return InlineArgument(
            "allowed_updates",
            [
                key
                for key, value in zip(
                    [
                        "message",
                        "edited_channel_post",
                        "callback_query",
                    ],
                    [
                        self._message,
                        self._edited_channel_post,
                        self._callback_query,
                    ],
                )
                if value
            ],
        ).to_dict()
