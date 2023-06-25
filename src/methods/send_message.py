from abc import ABC, abstractmethod
from typing import Any
from dacite import from_dict
from more_itertools import flatten

from methods.method import Method
from bot.inner_bot import Bot
from content import JsonRequestContent
from methods.raw_method import RawMethod
from tg_types.user.message import Message
from uri.method_uri import MethodURI


class AbstractMethodArgument(ABC):
    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        ...


class EmptyArgument(AbstractMethodArgument):
    def to_dict(self) -> dict[str, Any]:
        return {}


class MethodArgument(AbstractMethodArgument):
    DEFAULT = EmptyArgument


class MessageText(MethodArgument):
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


class MessageConfig(MethodArgument):
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
        return {
            "disable_web_page_preview": self.disable_web_page_preview,
            "disable_notification": self.disable_notification,
            "protect_content": self.protect_content,
        }


class ReplyingMessage(MethodArgument):
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


class InlineMethodArgument(MethodArgument):
    def __init__(self, key: str, value: Any) -> None:
        self._key = key
        self._value = value

    def to_dict(self) -> dict[str, Any]:
        return {self._key: self._value}


class MethodArguments(MethodArgument):
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


class SendMessage(Method[Message]):
    def __init__(
        self,
        bot: Bot,
        chat_id: int,
        text: MessageText,
        message_thread_id: AbstractMethodArgument = EmptyArgument(),
        # entities: list[MessageEntity]=[],
        config: AbstractMethodArgument = EmptyArgument(),
        reply: AbstractMethodArgument = EmptyArgument(),
        reply_markup: AbstractMethodArgument = EmptyArgument(),
    ) -> None:
        self._bot = bot
        self._chat_id = chat_id
        self._message_thread_id = message_thread_id
        self._text = text
        # self._entities = entities
        self._config = config
        self._reply = reply
        self.reply_markup = reply_markup

    def call(self) -> Message:
        print(self._chat_id)
        instance = from_dict(
            data_class=Message,
            data=RawMethod(
                MethodURI("sendMessage", self._bot),
                JsonRequestContent(
                    MethodArguments(
                        [
                            InlineMethodArgument(
                                "chat_id", self._chat_id
                            ),
                            self._message_thread_id,
                            self._text,
                            self._config,
                            self._reply,
                            self.reply_markup,
                        ]
                    ).to_dict()
                ),
            ).call(),
        )
        return instance  # type: ignore
