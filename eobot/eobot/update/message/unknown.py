from __future__ import annotations
from abc import ABC, abstractmethod
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from eobot.bot.inner_bot import Bot
from eobot.update.on_event import OnEvent
from eobot.update.update import Update
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eobot.tgtypes.message.unknown import UnknownMessage
    from eobot.update.events import Events


class UnknownMessageUpdate(Update):
    def __init__(
        self,
        update_id: int,
        message: UnknownMessage,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._id = update_id
        self._message = message
        self._log = log

    def id(self) -> int:
        return self._id

    def handle(self, bot: Bot, events: Events) -> None:
        self._log.info(f"MessageUpdate: {self._id} handle")
        events.handle_unknown_message(bot, self._message)


class OnUnknownMessage(OnEvent["UnknownMessage"]):
    @abstractmethod
    def handle(
        self, bot: Bot, message: "UnknownMessage"
    ) -> None:
        ...


class UnknownMessageWarning(OnUnknownMessage):
    def __init__(self, log: AbstractLog = NoLog()) -> None:
        self._log = log

    def handle(
        self, bot: Bot, message: "UnknownMessage"
    ) -> None:
        self._log.warning(
            (
                "Received unknown message. "
                "This message type is probably not "
                "implemented yet or is not supported"
            )
        )
