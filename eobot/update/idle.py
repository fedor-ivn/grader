from typing import TypeVar

from logger.no_log import NoLog
from logger.abstract_log import AbstractLog

from eobot.bot.bot import Bot
from eobot.tgtypes.message.message import Message
from eobot.update.on_event import OnEvent

T = TypeVar("T")


class Idle(OnEvent[Message[T]]):
    def __init__(
        self,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._log = log

    def handle(self, bot: Bot, message: Message[T]) -> bool:
        self._log.debug("Do Nothing")
        return True
