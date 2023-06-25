from bot.inner_bot import Bot, EnvironmentToken
from event_loop import EventLoop
from arguments.message.text import PlainText
from methods.get_me import GetMe
from methods.get_user_profile_photos import (
    GetUserProfilePhotos,
)
from methods.get_updates import GetUpdates
from methods.send_message import SendMessage
from update.handlers import Handlers, MessageHandler

from tgtypes.message.message import Message
from polling import Polling


class PrintMessageText(MessageHandler):
    def handle(self, bot: Bot, message: Message) -> None:
        print(message.text())
        bot.call_method(
            SendMessage(
                chat_id=742596099,
                text=PlainText(message.text()),
            )
        )


if __name__ == "__main__":
    Polling(
        Bot(EnvironmentToken("BOT_TOKEN")),
        EventLoop(
            Handlers(
                message_handlers=[
                    PrintMessageText(),
                    PrintMessageText(),
                ]
            )
        ),
    ).start()

# GetMe(bot).call()
# print(GetUserProfilePhotos(bot, user_id=742596099).call())

# print(
#     bot.call_method(
#         SendMessage(
#             chat_id=742596099,
#             text=PlainText("Hello!"),
#         )
#     )
# )

# print(
#     bot.call_method(
#         GetUpdates(
#             # chat_id=742596099,
#             # text=PlainText("Hello!"),
#         )
#     )
# )
