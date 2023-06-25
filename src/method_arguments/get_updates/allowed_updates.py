from method_arguments.method_argument import (
    AbstractMethodArgument,
)
from method_arguments.inline import InlineMethodArgument
from typing import Any


class AllowedUpdatesArgument(AbstractMethodArgument):
    def __init__(
        self,
        message: bool = True,
        edited_channel_post: bool = True,
        callback_query: bool = True,
    ) -> None:
        self._message = message
        self._edited_channel_post = edited_channel_post
        self._callback_query = callback_query

    def to_dict(self) -> dict[str, Any]:
        return InlineMethodArgument(
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
