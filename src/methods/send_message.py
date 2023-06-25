from method_arguments.method_argument import (
    AbstractMethodArgument,
)
from method_arguments.empty import EmptyArgument
from method_arguments.inline import InlineMethodArgument
from method_arguments.message.text import MessageText
from method_arguments.method_arguments import (
    MethodArguments,
)
from methods.method import Method
from bot.inner_bot import Bot
from content import JsonRequestContent
from methods.raw_method import RawMethod
from tgtypes.message.message import Message
from uri.method_uri import MethodURI
from uri.uri import URI


class SendMessage(Method[Message]):
    def __init__(
        self,
        chat_id: int,
        text: MessageText,
        message_thread_id: AbstractMethodArgument = EmptyArgument(),
        # entities: list[MessageEntity]=[],
        config: AbstractMethodArgument = EmptyArgument(),
        reply: AbstractMethodArgument = EmptyArgument(),
        reply_markup: AbstractMethodArgument = EmptyArgument(),
    ) -> None:
        self._chat_id = chat_id
        self._message_thread_id = message_thread_id
        self._text = text
        # self._entities = entities
        self._config = config
        self._reply = reply
        self.reply_markup = reply_markup

    def call(self, bot: URI) -> Message:
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
            ).call(MethodURI("sendMessage", bot)),
        )
        return instance  # type: ignore
