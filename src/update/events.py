from abc import ABC, abstractmethod
from bot.inner_bot import Bot
from tgtypes.message.message import Message

# from tgtypes.user.message import Message


class OnMessage(ABC):
    @abstractmethod
    def handle(self, bot: Bot, message: Message) -> None:
        ...


class Events:
    def __init__(
        self, on_message: list[OnMessage] = []
    ) -> None:
        self._message_handlers = on_message

    def handle_message(
        self, bot: Bot, message: Message
    ) -> None:
        for handler in self._message_handlers:
            handler.handle(bot, message)
