from abc import ABC, abstractmethod
from arguments.argument import MethodArgument
from arguments.inline import InlineArgument
from bot.inner_bot import Bot
from tgtypes.message.message import Message

from update.events import Events


class Update(ABC):
    @abstractmethod
    def id(self) -> int:
        ...

    @abstractmethod
    def handle(self, bot: Bot, handlers: Events) -> None:
        ...


class MessageUpdate(Update):
    def __init__(
        self, update_id: int, message: Message
    ) -> None:
        self._id = update_id
        self._message = message

    def id(self) -> int:
        return self._id

    def handle(self, bot: Bot, handlers: Events) -> None:
        handlers.handle_message(bot, self._message)
