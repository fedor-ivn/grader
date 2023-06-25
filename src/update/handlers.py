from abc import ABC, abstractmethod
from bot.inner_bot import Bot
from tgtypes.message.message import Message

# from tgtypes.user.message import Message


class MessageHandler(ABC):
    @abstractmethod
    def handle(self, bot: Bot, message: Message) -> None:
        ...


class Handlers:
    def __init__(
        self, message_handlers: list[MessageHandler] = []
    ) -> None:
        self._message_handlers = message_handlers

    def handle_message(
        self, bot: Bot, message: Message
    ) -> None:
        for handler in self._message_handlers:
            handler.handle(bot, message)
