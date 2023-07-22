import pprint
from typing import Any
from arguments.argument import (
    MethodArgument,
)
from arguments.inline import InlineArgument
from arguments.message.config import MessageConfig
from arguments.message.destination import Destination
from arguments.message.replying import (
    AbstractReplyingMessage,
    NoReplyingMessage,
)
from arguments.message.text import MessageText
from arguments.message.thread import (
    AbstractThreadId,
    NoThreadId,
)
from arguments.method_arguments import (
    MethodArguments,
)
from arguments.keyboard.keyboard import ReplyKeyboard
from arguments.keyboard.no_keyboard import NoKeyboard
from arguments.keyboard.abstract import AbstractKeyboard
from methods.method import Method
from content import JsonRequestContent
from methods.raw_method import RawMethod
from raw_types.message.message import RawMessage
from tgtypes.message.message import Message
from uri.method_uri import MethodURI
from uri.uri import URI
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class SendMessage(Method[Message[Any]]):
    def __init__(
        self,
        destination: Destination,
        text: MessageText,
        # entities: list[MessageEntity]=[],
        disable_web_page_preview: bool = False,
        config: MessageConfig = MessageConfig(),
        reply: AbstractReplyingMessage = NoReplyingMessage(),
        reply_markup: AbstractKeyboard = NoKeyboard(),
        log: AbstractLog = NoLog(),
    ) -> None:
        self._destination = destination
        self._text = text
        # self._entities = entities
        self._disable_web_page_preview = (
            disable_web_page_preview
        )
        self._config = config
        self._reply = reply
        self._reply_markup = reply_markup
        self._log = log

    def call(self, bot: URI) -> Message[Any]:
        arguments = MethodArguments(
            [
                self._destination,
                self._text,
                # self._entities,
                InlineArgument(
                    "disable_web_page_preview",
                    self._disable_web_page_preview,
                ),
                self._config,
                self._reply,
                InlineArgument(
                    "reply_markup",
                    self._reply_markup.to_dict(),
                ),
            ]
        ).to_dict()
        self._log.debug(pprint.pformat(arguments))

        return RawMessage(
            RawMethod(
                JsonRequestContent(arguments),
            ).call(MethodURI("sendMessage", bot)),
        ).parse()
