from bot.inner_bot import Bot
from update.events import Events
from update.update import Update
from update.updates import Updates


class EventLoop:
    def __init__(self, handlers: Events) -> None:
        self._handlers = handlers

    def handle_updates(
        self, bot: Bot, updates: Updates
    ) -> None:
        updates.handle(bot, self._handlers)
