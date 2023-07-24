import logging
import os
from typing import Any

from arguments.message.replying import ReplyingMessage
from eobot.bot.bot import Bot
from bot.token import DotenvToken
from eobot.bot.bot import Bot
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
from tgtypes.message.document import (
    DocumentMessage,
)
from polling import Polling, PollingConfig
from dotenv.main import DotEnv

from logger.log import LogConfig
from eobot.update.message.document import OnDocumentMessage
from update.message.unknown import (
    UnknownMessageWarning,
)


class GreetingText(MessageText):
    def to_dict(self) -> dict[str, Any]:
        return PlainText(
            """
This is document echo bot - an example of the usage of the eobot
library that we have created. The current example is
used for the showcase of the receiving and sending
the document messages.

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
    ) -> bool:
        bot.call_method(
            SendMessage(
                message.chat.create_destination(),
                GreetingText(),
                log=self._log,
            )
        )
        return True


class Echo(OnDocumentMessage):
    def __init__(
        self,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._log = log

    def handle(
        self, bot: Bot, message: DocumentMessage
    ) -> bool:
        fetched_document = bot.call_method(
            message.document.fetch()
        )

        with bot.open_document(fetched_document) as file:
            content = file.read().decode("utf-8")

            try:
                bot.call_method(
                    SendMessage(
                        message.chat.create_destination(),
                        PlainText(content),
                        reply=ReplyingMessage(message.id),
                    )
                )

                return True
            except Exception as e:
                print(e)
                return True


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
                        OnMatchedText(
                            "/start",
                            Hello(log=log),
                        ),
                    ],
                    on_document_message=[
                        Echo(
                            log=log,
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
