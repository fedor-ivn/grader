from typing import Any
from arguments.argument import MethodArgument
from arguments.inline import InlineArgument
from arguments.message.thread import (
    AbstractThreadId,
    NoThreadId,
)
from arguments.method_arguments import MethodArguments

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class Destination(MethodArgument):
    def __init__(
        self,
        chat_id: int,
        message_thread_id: AbstractThreadId = NoThreadId(),
        log: AbstractLog = NoLog(),
    ) -> None:
        self._chat_id = chat_id
        self._message_thread_id = message_thread_id
        self._log = log

    def to_dict(self) -> dict[str, Any]:
        self._log.info("Destination.to_dict()")
        return MethodArguments(
            [
                InlineArgument("chat_id", self._chat_id),
                self._message_thread_id,
            ]
        ).to_dict()
