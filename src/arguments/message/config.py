from typing import Any
from arguments.argument import (
    MethodArgument,
)

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class MessageConfig(MethodArgument):
    def __init__(
        self,
        disable_notification: bool = False,
        protect_content: bool = False,
        log: AbstractLog = NoLog(),
    ) -> None:
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.log = log

    def to_dict(self) -> dict[str, Any]:
        self.log.debug(
            "MessageConfig.to_dict()"
            f"disable_notification={self.disable_notification}"
            f"protect_content={self.protect_content}"
        )
        return {
            "disable_notification": self.disable_notification,
            "protect_content": self.protect_content,
        }
