from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from bot.inner_bot import Bot

T = TypeVar("T")


class OnEvent(ABC, Generic[T]):
    @abstractmethod
    def handle(self, bot: Bot, entity: T) -> bool:
        ...
