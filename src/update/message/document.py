from __future__ import annotations
from abc import ABC, abstractmethod
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from bot.inner_bot import Bot
from update.on_event import OnEvent
from update.update import Update
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from update.events import Events
    from tgtypes.message.document import DocumentMessage


class DocumentMessageUpdate(Update):
    def __init__(
        self,
        update_id: int,
        message: "DocumentMessage",
        log: AbstractLog = NoLog(),
    ) -> None:
        self._id = update_id
        self._message = message
        self._log = log

    def id(self) -> int:
        return self._id

    def handle(self, bot: Bot, events: Events) -> None:
        self._log.info(f"MessageUpdate: {self._id} handle")
        events.handle_document_message(bot, self._message)


class OnDocumentMessage(OnEvent["DocumentMessage"]):
    @abstractmethod
    def handle(
        self, bot: Bot, message: "DocumentMessage"
    ) -> None:
        ...
