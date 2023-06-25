from typing import Any
from arguments.argument import (
    MethodArgument,
)
from arguments.empty import EmptyArgument


class MessageConfig(MethodArgument):
    def __init__(
        self,
        disable_web_page_preview: bool = False,
        disable_notification: bool = False,
        protect_content: bool = False,
        reply_markup: MethodArgument = EmptyArgument(),
    ) -> None:
        self.disable_web_page_preview = (
            disable_web_page_preview
        )
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_markup = reply_markup

    def to_dict(self) -> dict[str, Any]:
        args = {
            "disable_web_page_preview": self.disable_web_page_preview,
            "disable_notification": self.disable_notification,
            "protect_content": self.protect_content,
        }
        args.update(self.reply_markup.to_dict())
        return args
