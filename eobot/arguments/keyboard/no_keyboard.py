from typing import Any
from arguments.keyboard.abstract import AbstractKeyboard


class NoKeyboard(AbstractKeyboard):
    def to_dict(self) -> dict[str, Any]:
        return {}
