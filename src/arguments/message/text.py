from arguments.argument import (
    MethodArgument,
)
from typing import Any

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class MessageText(MethodArgument):
    pass


class PlainText(MessageText):
    def __init__(
        self,
        text: str,
    ) -> None:
        self.text = text

    def to_dict(self) -> dict[str, Any]:
        return {"text": self.text}


class MarkdownText(MessageText):
    def __init__(
        self,
        text: str,
    ) -> None:
        self.text = text

    def to_dict(self) -> dict[str, Any]:
        return {"text": self.text, "parse_mode": "Markdown"}


class MarkdownV2Text(MessageText):
    def __init__(
        self,
        text: str,
    ) -> None:
        self.text = text

    def to_dict(self) -> dict[str, Any]:
        return {
            "text": self.text,
            "parse_mode": "MarkdownV2",
        }


class HTMLText(MessageText):
    def __init__(
        self,
        text: str,
    ) -> None:
        self.text = text

    def to_dict(self) -> dict[str, Any]:
        return {"text": self.text, "parse_mode": "HTML"}
