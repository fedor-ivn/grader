from __future__ import annotations
from abc import ABC, abstractmethod
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from bot.inner_bot import Bot
from update.update import Update
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from update.events import Events
    from tgtypes.message.message import TextMessage


class TextMessageUpdate(Update):
    def __init__(
        self,
        update_id: int,
        message: TextMessage,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._id = update_id
        self._message = message
        self._log = log

    def id(self) -> int:
        return self._id

    def handle(self, bot: Bot, events: Events) -> None:
        self._log.info(f"MessageUpdate: {self._id} handle")
        events.handle_text_message(bot, self._message)


class OnTextMessage(ABC):
    @abstractmethod
    def handle(
        self, bot: Bot, message: TextMessage
    ) -> None:
        ...
