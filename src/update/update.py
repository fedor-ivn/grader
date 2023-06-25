from abc import ABC, abstractmethod
from bot.inner_bot import Bot
from tgtypes.message.message import Message

from update.handlers import Handlers


class Update(ABC):
    def __init__(self, update_id: int) -> None:
        self._update_id = update_id

    @abstractmethod
    def handle(self, bot: Bot, handlers: Handlers) -> None:
        ...


class MessageUpdate(Update):
    def __init__(
        self, update_id: int, message: Message
    ) -> None:
        super().__init__(update_id)
        self._message = message

    def handle(self, bot: Bot, handlers: Handlers) -> None:
        handlers.handle_message(bot, self._message)
