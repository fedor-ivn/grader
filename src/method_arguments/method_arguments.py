"""
todo:  Дамир, распили этот файл на мелкие файлы плз
"""


from abc import ABC, abstractmethod
from typing import Any

from more_itertools import flatten


class AbstractMethodArgument(ABC):
    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        ...


class EmptyArgument(AbstractMethodArgument):
    def to_dict(self) -> dict[str, Any]:
        return {}


class MessageText(AbstractMethodArgument):
    pass


class PlainText(MessageText):
    def __init__(self, text: str) -> None:
        self.text = text

    def to_dict(self) -> dict[str, Any]:
        return {"text": self.text}


class MarkdownText(MessageText):
    def __init__(self, text: str) -> None:
        self.text = text

    def to_dict(self) -> dict[str, Any]:
        return {"text": self.text, "parse_mode": "Markdown"}


class MarkdownV2Text(MessageText):
    def __init__(self, text: str) -> None:
        self.text = text

    def to_dict(self) -> dict[str, Any]:
        return {
            "text": self.text,
            "parse_mode": "MarkdownV2",
        }


class HTMLText(MessageText):
    def __init__(self, text: str) -> None:
        self.text = text

    def to_dict(self) -> dict[str, Any]:
        return {"text": self.text, "parse_mode": "HTML"}


class MessageConfig(AbstractMethodArgument):
    def __init__(
        self,
        disable_web_page_preview: bool = False,
        disable_notification: bool = False,
        protect_content: bool = False,
        reply_markup: AbstractMethodArgument = EmptyArgument(),
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


class InlineMethodArgument(AbstractMethodArgument):
    def __init__(self, key: str, value: Any) -> None:
        self._key = key
        self._value = value

    def to_dict(self) -> dict[str, Any]:
        return {self._key: self._value}


class MethodArguments(AbstractMethodArgument):
    def __init__(
        self, methods: list[AbstractMethodArgument]
    ) -> None:
        self.methods = methods

    def to_dict(self) -> dict[str, Any]:
        return dict(
            flatten(
                [
                    method.to_dict().items()
                    for method in self.methods
                ]
            )
        )
