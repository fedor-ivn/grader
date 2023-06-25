from abc import ABC, abstractmethod
from typing import Any
from dacite import from_dict
from more_itertools import flatten
from method_arguments.method_arguments import (
    AbstractMethodArgument,
    EmptyArgument,
    InlineMethodArgument,
    MessageText,
    MethodArguments,
)

from methods.method import Method
from bot.inner_bot import Bot
from content import JsonRequestContent
from methods.raw_method import RawMethod
from tg_types.user.message import Message
from uri.method_uri import MethodURI


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
        # instance = from_dict(
        #     data_class=Message,
        #     data=RawMethod(
        #         MethodURI("sendMessage", self._bot),
        #         JsonRequestContent(
        #             MethodArguments(
        #                 [
        #                     InlineMethodArgument(
        #                         "chat_id", self._chat_id
        #                     ),
        #                     self._message_thread_id,
        #                     self._text,
        #                     self._config,
        #                     self._reply,
        #                     self.reply_markup,
        #                 ]
        #             ).to_dict()
        #         ),
        #     ).call(),
        # )
        instance = (
            RawMethod(
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
