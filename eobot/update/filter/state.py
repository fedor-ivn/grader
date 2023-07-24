from __future__ import annotations
from typing import TYPE_CHECKING, Generic, Self, TypeVar

from logger.no_log import NoLog
from logger.abstract_log import AbstractLog

from eobot.bot.bot import Bot
from eobot.fsm.user_state.abstract import AbstractUserStates
from eobot.fsm.user_state.dummy import DummyUserStates
from eobot.tgtypes.message.message import Message
from eobot.update.idle import Idle
from eobot.update.on_event import OnEvent

if TYPE_CHECKING:
    from eobot.fsm.user_state.state import UserStates

T = TypeVar("T")


class OnState(OnEvent[Message[T]]):
    def __init__(
        self,
        state_name: str,
        user_states: AbstractUserStates[
            T
        ] = DummyUserStates(),
        on_event: OnEvent[Message[T]] = Idle(),
        log: AbstractLog = NoLog(),
    ) -> None:
        self.user_states = user_states
        self.name = state_name
        self._on_event = on_event
        self._log = log

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name  # type: ignore

    def with_states(
        self, user_states: UserStates[T]
    ) -> "OnState[T]":
        return OnState(
            self.name,
            user_states,
            self._on_event,
            self._log,
        )

    def do(
        self, on_event: OnEvent[Message[T]]
    ) -> "OnState[T]":
        return OnState(
            self.name,
            self.user_states,
            on_event,
            self._log,
        )

    def handle(self, bot: Bot, message: Message[T]) -> bool:
        self._log.debug(
            "Try to handle the message on state"
        )
        print(type(self.user_states.state(message.chat.id)))
        self._log.debug(
            f"name: {self.user_states.state(message.chat.id).name}"
        )

        if self.user_states.match(message.chat.id, self):
            self._log.debug("Message matched")
            return self._on_event.handle(bot, message)

        self._log.debug("Message not matched")
        return False
