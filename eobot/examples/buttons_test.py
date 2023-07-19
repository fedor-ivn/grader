import logging
import os
from typing import Any

from bot.inner_bot import Bot
from bot.token import DotenvToken
from bot.inner_bot import Bot
from eobot.update.filter.text import OnMatchedText
from tgtypes.message.text import TextMessage
from eobot.update.message.text import OnTextMessage
from event_loop import EventLoop
from eobot.arguments.message.text import (
    MessageText,
    PlainText,
)
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from methods.send_message import SendMessage
from update.events import Events
from polling import Polling, PollingConfig
from dotenv.main import DotEnv

from logger.log import LogConfig
from update.message.unknown import (
    UnknownMessageWarning,
)

from arguments.keyboard.button import Button
from arguments.keyboard.keyboard import ReplyKeyboard


class GreetingText(MessageText):
    def to_dict(self) -> dict[str, Any]:
        return PlainText(
            """
This is button echo bot - an example of the usage of the eobot
library that we have created. The current example is 
used for the showcase of the creating the keyboard buttons.

In case of any problems, do not hesitate to contact the
developers:

- @fedor_ivn
- @Probirochniy
"""
        ).to_dict()


class Hello(OnTextMessage):
    def __init__(
        self,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._log = log

    def handle(
        self, bot: Bot, message: TextMessage
    ) -> None:
        bot.call_method(
            SendMessage(
                message.chat.create_destination(),
                GreetingText(),
                log=self._log,
            )
        )


class ButtonEcho(OnTextMessage):
    def __init__(self, log: AbstractLog = NoLog()) -> None:
        self._log = log

    def handle(
        self, bot: Bot, message: TextMessage
    ) -> None:
        bot.call_method(
            SendMessage(
                message.chat.create_destination(),
                PlainText("Button created!"),
                reply_markup=ReplyKeyboard([[Button(message.text.value)]]),
                log=self._log,
            )
        )


if __name__ == "__main__":
    log = LogConfig(
        level=logging.DEBUG,
        format="%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    ).configure()
    script_path = os.path.abspath(os.path.dirname(__file__))

    Bot(DotenvToken("BOT_TOKEN", DotEnv(".env"))).start(
        Polling(
            EventLoop(
                Events(
                    on_text_message=[
                        ButtonEcho(log=log),
                        OnMatchedText(
                            "/start",
                            Hello(log=log),
                        ),
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
