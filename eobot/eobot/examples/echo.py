import logging
from dotenv.main import DotEnv

from logger.log import LogConfig
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog

from arguments.message.text import PlainText
from bot.inner_bot import Bot
from bot.token import DotenvToken
from event_loop import EventLoop
from methods.send_message import SendMessage
from polling import Polling, PollingConfig
from tgtypes.message.text import TextMessage
from update.events import Events
from update.message.text import OnTextMessage


class Echo(OnTextMessage):
    def __init__(self, log: AbstractLog = NoLog()) -> None:
        self._log = log

    def handle(
        self, bot: Bot, message: TextMessage
    ) -> None:
        bot.call_method(
            SendMessage(
                message.chat.create_destination(),
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
                    on_text_message=[
                        Echo(log=log),
                    ],
                    log=log,
                ),
                log=log,
            ),
            PollingConfig(log=log),
            log=log,
        ),
    )
