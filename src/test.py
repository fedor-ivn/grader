import logging
from bot.inner_bot import Bot
from bot.token import DotenvToken
from event_loop import EventLoop
from arguments.message.text import PlainText
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from methods.send_message import SendMessage
from update.events import Events


from tgtypes.message.message import (
    DocumentMessage,
)
from polling import Polling, PollingConfig
from dotenv.main import DotEnv

from logger.log import LogConfig
from update.message.document import OnDocumentMessage
from update.message.unknown import UnknownMessageWarning


class GradeTask(OnDocumentMessage):
    def __init__(self, log: AbstractLog = NoLog()) -> None:
        self._log = log

    def handle(
        self, bot: Bot, message: DocumentMessage
    ) -> None:
        print(message.document.file_id)
        with bot.open_document(message.document) as file:
            print(file.read())


if __name__ == "__main__":
    log = LogConfig(
        level=logging.ERROR,
        format="%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    ).configure()

    Bot(DotenvToken("BOT_TOKEN", DotEnv(".env"))).start(
        Polling(
            EventLoop(
                Events(
                    on_document_message=[
                        GradeTask(log=log),
                    ],
                    on_unknown_message=[
                        UnknownMessageWarning(log=log),
                    ],
                    log=log,
                ),
                log=log,
            ),
            PollingConfig(log=log),
            log=log,
        ),
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
