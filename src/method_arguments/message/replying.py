from typing import Any
from method_arguments.method_argument import (
    AbstractMethodArgument,
)


class ReplyingMessage(AbstractMethodArgument):
    def __init__(
        self,
        reply_to_message_id: int,
        allow_sending_without_reply: bool = False,
    ) -> None:
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = (
            allow_sending_without_reply
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "reply_to_message_id": self.reply_to_message_id,
            "allow_sending_without_reply": self.allow_sending_without_reply,
        }
