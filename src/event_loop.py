from bot.inner_bot import Bot
from update.handlers import Handlers
from update.update import Update


class EventLoop:
    def __init__(self, handlers: Handlers) -> None:
        self._handlers = handlers

    def handle_updates(
        self, bot: Bot, updates: list[Update]
    ) -> None:
        for update in updates:
            update.handle(bot, self._handlers)
