from typing import Any
from arguments.argument import (
    MethodArgument,
)

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class AbstractReplyingMessage(MethodArgument):
    pass


class NoReplyingMessage(AbstractReplyingMessage):
    def to_dict(self) -> dict[str, Any]:
        return {}


class ReplyingMessage(AbstractReplyingMessage):
    def __init__(
        self,
        reply_to_message_id: int,
        allow_sending_without_reply: bool = False,
        log: AbstractLog = NoLog(),
    ) -> None:
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = (
            allow_sending_without_reply
        )
        self._log = log

    def to_dict(self) -> dict[str, int | bool]:
        self._log.debug(
            "ReplyingMessage.to_dict"
            f" reply_to_message_id: {self.reply_to_message_id}"
            f" allow_sending_without_reply: {self.allow_sending_without_reply}"
        )
        return {
            "reply_to_message_id": self.reply_to_message_id,
            "allow_sending_without_reply": self.allow_sending_without_reply,
        }
