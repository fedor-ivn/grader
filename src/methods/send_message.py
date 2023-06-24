from dacite import from_dict

from methods.method import Method
from bot.inner_bot import Bot
from content import JsonContent
from methods.raw_method import RawMethod
from tg_types.user.message import Message
from uri.method_uri import MethodURI


class SendMessage(Method[Message]):
    def __init__(
        self,
        bot: Bot,
        chat_id: int,
        message_thread_id=None,
        text="",
        parse_mode=None,
        entities=None,
        disable_web_page_preview=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=False,
        reply_markup=None,
    ) -> None:
        self._bot = bot
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.text = text
        self.parse_mode = parse_mode
        self.entities = entities
        self.disable_web_page_preview = (
            disable_web_page_preview
        )
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = (
            allow_sending_without_reply
        )
        self.reply_markup = reply_markup

    def call(self) -> Message:

        print(self.chat_id)
        instance = from_dict(
            data_class=Message,
            data=RawMethod(
                MethodURI("sendMessage", self._bot),
                JsonContent(
                    {
                        "chat_id": self.chat_id,
                        "message_thread_id": self.message_thread_id,
                        "text": self.text,
                        "parse_mode": self.parse_mode,
                        "entities": self.entities,
                        "disable_web_page_preview": self.disable_web_page_preview,
                        "disable_notification": self.disable_notification,
                        "protect_content": self.protect_content,
                        "reply_to_message_id": self.reply_to_message_id,
                        "allow_sending_without_reply": self.allow_sending_without_reply,
                        "reply_markup": self.reply_markup,
                    }
                ),
            ).call(),
        )
        return instance  # type: ignore
