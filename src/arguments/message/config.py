from typing import Any
from arguments.argument import (
    MethodArgument,
)


class MessageConfig(MethodArgument):
    def __init__(
        self,
        disable_notification: bool = False,
        protect_content: bool = False,
    ) -> None:
        self.disable_notification = disable_notification
        self.protect_content = protect_content

    def to_dict(self) -> dict[str, Any]:
        return {
            "disable_notification": self.disable_notification,
            "protect_content": self.protect_content,
        }
