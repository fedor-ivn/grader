from typing import Generic, TypeVar

from vedis import Vedis

from logger.no_log import NoLog
from logger.abstract_log import AbstractLog

from eobot.bot.inner_bot import Bot
from eobot.tgtypes.message.message import Message
from eobot.update.on_event import OnEvent
from eobot.fsm.user_state import UserStates

T = TypeVar("T")


class OnState(OnEvent[Message[T]]):
    def __init__(
        self,
        state: str,
        user_states: UserStates,
        on_event: OnEvent[Message[T]],
        log: AbstractLog = NoLog(),
    ) -> None:
        self.user_states = user_states
        self.state = state
        self._on_event = on_event
        self._log = log

    def handle(self, bot: Bot, message: Message[T]) -> bool:
        self._log.debug(
            "Try to handle the message on state"
        )

        if self.user_states.match(
            message.chat.id, self.state
        ):
            self._log.debug("Text message matched")
            return self._on_event.handle(bot, message)

        self._log.debug("Text message not matched")
        return False
