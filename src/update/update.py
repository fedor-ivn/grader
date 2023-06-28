from abc import ABC, abstractmethod
from arguments.argument import MethodArgument
from arguments.inline import InlineArgument
from bot.inner_bot import Bot
from tgtypes.message.message import Message

from update.events import Events

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class Update(ABC):
    @abstractmethod
    def id(self) -> int:
        ...

    @abstractmethod
    def handle(self, bot: Bot, handlers: Events) -> None:
        ...


class MessageUpdate(Update):
    def __init__(
        self,
        update_id: int,
        message: Message,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._id = update_id
        self._message = message
        self.log = log

    def id(self) -> int:
        self.log.info(f"MessageUpdate: {self._id}")
        return self._id

    def handle(self, bot: Bot, handlers: Events) -> None:
        self.log.info(f"MessageUpdate: {self._id} handle")
        handlers.handle_message(bot, self._message)
