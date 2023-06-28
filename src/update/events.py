from bot.inner_bot import Bot
from tgtypes.message.message import TextMessage
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog

from update.message.text import OnTextMessage


class Events:
    def __init__(
        self,
        on_text_message: list[OnTextMessage] = [],
        log: AbstractLog = NoLog(),
    ) -> None:
        self._on_text_message = on_text_message
        self._log = log

    def handle_text_message(
        self, bot: Bot, message: TextMessage
    ) -> None:
        self._log.info(f"Handling message {message}...")
        for handler in self._on_text_message:
            self._log.info(
                f"Handling message with {handler}"
            )
            handler.handle(bot, message)
