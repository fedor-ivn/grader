from abc import ABC, abstractmethod
from bot.inner_bot import Bot
from tgtypes.message.message import Message
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog

# from tgtypes.user.message import Message


class OnMessage(ABC):
    @abstractmethod
    def handle(self, bot: Bot, message: Message) -> None:
        ...


class Events:
    def __init__(
        self,
        on_message: list[OnMessage] = [],
        log: AbstractLog = NoLog(),
    ) -> None:
        self._message_handlers = on_message
        self.log = log

    def handle_message(
        self, bot: Bot, message: Message
    ) -> None:
        self.log.info(f"Handling message {message}...")
        for handler in self._message_handlers:
            self.log.info(
                f"Handling message with {handler}"
            )
            handler.handle(bot, message)
