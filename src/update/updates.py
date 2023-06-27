from typing import Sequence
from arguments.argument import MethodArgument
from bot.inner_bot import Bot
from exceptions import NoUpdatesException
from update.events import Events
from update.update import Update
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class Updates:
    def __init__(
        self,
        updates: Sequence[Update],
        log: AbstractLog = NoLog(),
    ) -> None:
        self._updates = updates
        self.log = log

    def handle(self, bot: Bot, handlers: Events) -> None:
        self.log.info("Handling updates")
        for update in self._updates:
            update.handle(bot, handlers)

    def update_offset(self, old: int) -> int:
        self.log.info("Updating offset")
        if len(self._updates) == 0:
            return old
        last_update = self._updates[-1]
        return last_update.id() + 1
