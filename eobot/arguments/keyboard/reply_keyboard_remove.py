from typing import Any
from eobot.arguments.keyboard.abstract import (
    AbstractKeyboard,
)


class ReplyKeyboardRemove(AbstractKeyboard):
    def __init__(self, selective: bool = False) -> None:
        self._selective = selective

    def to_dict(self) -> dict[str, Any]:
        return {
            "remove_keyboard": True,
            "selective": self._selective,
        }