from abc import ABC, abstractmethod
from arguments.argument import MethodArgument
from arguments.inline import InlineArgument
from bot.inner_bot import Bot
from tgtypes.message.message import Message

from update.handlers import Handlers


class Update(ABC):
    def __init__(self, update_id: int) -> None:
        self._id = update_id

    @abstractmethod
    def updated_offset(self) -> MethodArgument:
        ...

    @abstractmethod
    def handle(self, bot: Bot, handlers: Handlers) -> None:
        ...


class MessageUpdate(Update):
    def __init__(
        self, update_id: int, message: Message
    ) -> None:
        super().__init__(update_id)
        self._message = message

    def updated_offset(self) -> MethodArgument:
        return InlineArgument("offset", self._id + 1)

    def handle(self, bot: Bot, handlers: Handlers) -> None:
        handlers.handle_message(bot, self._message)
