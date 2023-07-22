from typing import Any
from arguments.keyboard.button import Button
from eobot.arguments.keyboard.abstract import (
    AbstractKeyboard,
)
from eobot.arguments.keyboard.keyboard import ReplyKeyboard


class GridKeyboard(AbstractKeyboard):
    def __init__(
        self, buttons_list: list[Button], row_len: int
    ) -> None:
        self._buttons_list = buttons_list
        self._row_len = row_len

    def to_dict(self) -> dict[str, Any]:
        return ReplyKeyboard(
            [
                self._buttons_list[i : i + self._row_len]
                for i in range(
                    0,
                    len(self._buttons_list),
                    self._row_len,
                )
            ]
        ).to_dict()
