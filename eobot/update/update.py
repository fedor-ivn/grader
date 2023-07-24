from __future__ import annotations
from abc import ABC, abstractmethod
from arguments.argument import MethodArgument
from arguments.inline import InlineArgument
from eobot.bot.bot import Bot


from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from update.events import Events


class Update(ABC):
    @abstractmethod
    def id(self) -> int:
        ...

    @abstractmethod
    def handle(self, bot: Bot, events: Events) -> None:
        ...
