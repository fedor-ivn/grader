from bot.inner_bot import Bot
from bot.token import DotenvToken
from event_loop import EventLoop
from arguments.message.text import PlainText
from methods.get_me import GetMe
from methods.get_user_profile_photos import (
    GetUserProfilePhotos,
)
from methods.get_updates import GetUpdates
from methods.send_message import SendMessage
from update.events import Events, OnMessage

from tgtypes.message.message import Message
from polling import Polling
from dotenv.main import DotEnv


class PrintMessageText(OnMessage):
    def handle(self, bot: Bot, message: Message) -> None:
        print(message.text())
        bot.call_method(
            SendMessage(
                chat_id=742596099,
                text=PlainText(message.text()),
            )
        )


if __name__ == "__main__":
    Bot(DotenvToken("BOT_TOKEN", DotEnv(".env"))).start(
        Polling(
            EventLoop(
                Events(
                    on_message=[
                        PrintMessageText(),
                        PrintMessageText(),
                    ]
                )
            ),
        )
    )

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
