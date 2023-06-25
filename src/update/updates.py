from arguments.argument import MethodArgument
from arguments.empty import EmptyArgument
from bot.inner_bot import Bot
from update.handlers import Handlers
from update.update import Update


class Updates(Update):
    def __init__(self, updates: list[Update]) -> None:
        self._updates = updates

    def handle(self, bot: Bot, handlers: Handlers) -> None:
        for update in self._updates:
            update.handle(bot, handlers)

    def updated_offset(self) -> MethodArgument:
        if not self._updates:
            return EmptyArgument()
        last_update = self._updates[-1]
        return last_update.updated_offset()
