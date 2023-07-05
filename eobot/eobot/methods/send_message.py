from typing import Any
from eobot.arguments.argument import (
    MethodArgument,
)
from eobot.arguments.inline import InlineArgument
from eobot.arguments.message.config import MessageConfig
from eobot.arguments.message.destination import Destination
from eobot.arguments.message.replying import (
    AbstractReplyingMessage,
    NoReplyingMessage,
)
from eobot.arguments.message.text import MessageText
from eobot.arguments.message.thread import (
    AbstractThreadId,
    NoThreadId,
)
from eobot.arguments.method_arguments import (
    MethodArguments,
)
from eobot.methods.method import Method
from eobot.content import JsonRequestContent
from eobot.methods.raw_method import RawMethod
from eobot.raw_types.message.message import RawMessage
from eobot.tgtypes.message.message import Message
from eobot.uri.method_uri import MethodURI
from eobot.uri.uri import URI
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
        # reply_markup: MethodArgument = NoMarkup(),
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
        # self.reply_markup = reply_markup
        self._log = log

    def call(self, bot: URI) -> Message[Any]:
        return RawMessage(
            RawMethod(
                JsonRequestContent(
                    MethodArguments(
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
                            # self.reply_markup,
                        ]
                    ).to_dict()
                ),
            ).call(MethodURI("sendMessage", bot)),
        ).parse()
