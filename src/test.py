import logging
from arguments.message.destination import Destination
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

from tgtypes.message.message import Message, TextMessage
from polling import Polling
from dotenv.main import DotEnv

from logger.log import LogConfig


class PrintMessageText(OnMessage):
    def handle(
        self, bot: Bot, message: TextMessage
    ) -> None:
        print(message.text.value)
        bot.call_method(
            SendMessage(
                Destination(chat_id=742596099),
                text=PlainText(message.text.value),
            )
        )


if __name__ == "__main__":
    log = LogConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    ).configure()
    Bot(DotenvToken("BOT_TOKEN", DotEnv(".env"))).start(
        Polling(
            EventLoop(
                Events(
                    on_message=[
                        PrintMessageText(),
                        PrintMessageText(),
                    ],
                    log=log,
                ),
                log=log,
            ),
            log=log,
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
