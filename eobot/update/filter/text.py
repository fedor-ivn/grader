from eobot.bot.inner_bot import Bot
from eobot.tgtypes.message.text import TextMessage
from eobot.update.message.text import OnTextMessage
from logger.abstract_log import AbstractLog

from logger.no_log import NoLog


class OnMatchedText(OnTextMessage):
    def __init__(
        self,
        regex: str,
        on_event: OnTextMessage,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._on_event = on_event
        self._regex = regex
        self._log = log

    def handle(
        self, bot: Bot, message: TextMessage
    ) -> bool:
        self._log.debug("Try to match text message")
        self._log.debug(f"Text message: {message.text}")

        if message.text.match(self._regex):
            self._log.debug("Text message matched")
            return self._on_event.handle(bot, message)

        self._log.debug("Text message not matched")
        return False
