from typing import Any
from arguments.argument import MethodArgument
from arguments.inline import InlineArgument
from arguments.message.thread import (
    AbstractThreadId,
    NoThreadId,
)
from arguments.method_arguments import MethodArguments


class Destination(MethodArgument):
    def __init__(
        self,
        chat_id: int,
        message_thread_id: AbstractThreadId = NoThreadId(),
    ) -> None:
        self._chat_id = chat_id
        self._message_thread_id = message_thread_id

    def to_dict(self) -> dict[str, Any]:
        return MethodArguments(
            [
                InlineArgument("chat_id", self._chat_id),
                self._message_thread_id,
            ]
        ).to_dict()
