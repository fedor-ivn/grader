from abc import ABC, abstractmethod
from arguments.get_updates.allowed_updates import (
    AbstractAllowedUpdates,
    DefaultAllowedUpdates,
)
from eobot.state import State
from time import sleep
from arguments.argument import MethodArgument
from arguments.inline import InlineArgument
from arguments.merged import MergedArgument
from eobot.bot.bot import Bot
from event_loop import EventLoop
from methods.get_updates import GetUpdates
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class PollingConfig:
    def __init__(
        self,
        offset: int = -1,
        limit: int = 100,
        timeout: int = 0,
        allowed_updates: AbstractAllowedUpdates = DefaultAllowedUpdates(),
        log: AbstractLog = NoLog(),
    ) -> None:
        self._offset = offset
        self._limit = limit
        self._timeout = timeout
        self._allowed_updates = allowed_updates
        self._log = log

    def method(self) -> GetUpdates:
        return GetUpdates(
            self._offset,
            self._limit,
            self._timeout,
            self._allowed_updates,
            self._log,
        )

    def with_offset(self, offset: int) -> "PollingConfig":
        return PollingConfig(
            offset,
            self._limit,
            self._timeout,
            self._allowed_updates,
            self._log,
        )


class Polling(State):
    def __init__(
        self,
        event_loop: EventLoop,
        config: PollingConfig = PollingConfig(),
        poll_interval_ms: int = 25,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._event_loop = event_loop
        self._config = config
        self._poll_interval = poll_interval_ms
        self._log = log

    def start(self, bot: Bot) -> None:
        current_offset = 0

        while True:
            try:
                updates = bot.call_method(
                    self._config.method()
                )
                self._event_loop.handle_updates(
                    bot, updates
                )
                self._config = self._config.with_offset(
                    updates.update_offset(current_offset)
                )
                # is it okay to divide by 1000 inplace?
                sleep(self._poll_interval / 1000)
            except KeyboardInterrupt:
                break
