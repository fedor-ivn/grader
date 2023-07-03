from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Any,
    Generic,
    Sequence,
    TypeVar,
)
from bot.inner_bot import Bot

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from update.message.text import OnTextMessage
from update.message.unknown import (
    UnknownMessageWarning,
    OnUnknownMessage,
)
from update.on_event import OnEvent


if TYPE_CHECKING:
    from tgtypes.message.unknown import UnknownMessage
    from tgtypes.message.document import (
        DocumentMessage,
    )

    from tgtypes.message.text import (
        TextMessage,
    )

    from update.message.document import OnDocumentMessage

T = TypeVar("T")


class Event(Generic[T]):
    def __init__(
        self,
        on_event: Sequence[OnEvent[T]],
        log: AbstractLog = NoLog(),
    ) -> None:
        self._on_event = on_event
        self._log = log

    def handle(self, bot: Bot, entity: T) -> None:
        self._log.info(f"Handling message {entity}...")
        for handler in self._on_event:
            self._log.info(
                f"Handling entity with {handler}"
            )
            handler.handle(bot, entity)


class Events:
    def __init__(
        self,
        on_text_message: list[OnTextMessage] = [],
        on_document_message: list[OnDocumentMessage] = [],
        on_unknown_message: list[OnUnknownMessage] = [],
        log: AbstractLog = NoLog(),
    ) -> None:
        self._on_text_message = on_text_message
        self._on_document_message = on_document_message
        self._on_unknown_message = on_unknown_message
        self._log = log

    def handle_text_message(
        self, bot: Bot, message: TextMessage
    ) -> None:
        Event(self._on_text_message, self._log).handle(
            bot, message
        )

    def handle_document_message(
        self, bot: Bot, message: DocumentMessage
    ) -> None:
        Event(self._on_document_message, self._log).handle(
            bot, message
        )

    def handle_unknown_message(
        self, bot: Bot, message: UnknownMessage
    ) -> None:
        Event(self._on_unknown_message, self._log).handle(
            bot, message
        )
