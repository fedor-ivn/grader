from eobot.bot.inner_bot import Bot
from eobot.update.events import Events
from eobot.update.update import Update
from eobot.update.updates import Updates
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class EventLoop:
    def __init__(
        self, handlers: Events, log: AbstractLog = NoLog()
    ) -> None:
        self._handlers = handlers
        self._log = log

    def handle_updates(
        self, bot: Bot, updates: Updates
    ) -> None:
        self._log.info("Handling updates")
        updates.handle(bot, self._handlers)
