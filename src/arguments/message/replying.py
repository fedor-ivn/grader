from typing import Any
from arguments.argument import (
    MethodArgument,
)


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
    ) -> None:
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = (
            allow_sending_without_reply
        )

    def to_dict(self) -> dict[str, int | bool]:
        return {
            "reply_to_message_id": self.reply_to_message_id,
            "allow_sending_without_reply": self.allow_sending_without_reply,
        }
