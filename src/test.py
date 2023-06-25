from bot.inner_bot import Bot
from event_loop import EventLoop
from method_arguments.message.text import PlainText
from methods.get_me import GetMe
from methods.get_user_profile_photos import (
    GetUserProfilePhotos,
)
from methods.get_updates import GetUpdates
from update.handlers import Handlers, MessageHandler

from tgtypes.message.message import Message


class PrintMessageText(MessageHandler):
    def handle(self, bot: Bot, message: Message) -> None:
        print(message.text)


# EventLoop(
#     Bot(""),
#     Handlers(
#         message_handlers=[
#             PrintMessageText(),
#             PrintMessageText(),
#         ]
#     ),
# )

bot = Bot("5603622755:AAGW1Dmj72BsdwsJngxn-U5yMPfoqMCBxfI")
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

print(
    bot.call_method(
        GetUpdates(
            # chat_id=742596099,
            # text=PlainText("Hello!"),
        )
    )
)
