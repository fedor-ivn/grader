from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eobot.bot.bot import Bot


class State(ABC):
    @abstractmethod
    def start(self, bot: Bot) -> None:
        ...
