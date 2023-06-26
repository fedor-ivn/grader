from arguments.argument import (
    MethodArgument,
)
from arguments.inline import InlineArgument
from arguments.message.config import MessageConfig
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
        message_thread_id: AbstractThreadId = NoThreadId(),
        # entities: list[MessageEntity]=[],
        disable_web_page_preview: bool = False,
        config: MessageConfig = MessageConfig(),
        reply: AbstractReplyingMessage = NoReplyingMessage(),
        # reply_markup: MethodArgument = NoMarkup(),
    ) -> None:
        self._chat_id = chat_id
        self._message_thread_id = message_thread_id
        self._text = text
        # self._entities = entities
        self._disable_web_page_preview = (
            disable_web_page_preview
        )
        self._config = config
        self._reply = reply
        # self.reply_markup = reply_markup

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
                            InlineArgument(
                                "chat_id", self._chat_id
                            ),
                            self._message_thread_id,
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
        )
        return instance  # type: ignore
