from typing import Any
from arguments.keyboard.abstract import AbstractKeyboard
from arguments.keyboard.button import Button
from eobot.arguments.method_arguments import MethodArguments


class ReplyKeyboard(AbstractKeyboard):
    def __init__(
        self,
        keyboard: list[list[Button]],
        is_persistent: bool = False,
        resize_keyboard: bool = False,
        one_time_keyboard: bool = False,
        input_field_placeholder: str = "",
        selective: bool = False,
    ) -> None:
        self._keyboard = keyboard
        self._is_persistent = is_persistent
        self._resize_keyboard = resize_keyboard
        self._one_time_keyboard = one_time_keyboard
        self._input_field_placeholder = (
            input_field_placeholder
        )
        self._selective = selective

    def to_dict(self) -> dict[str, Any]:
        return {
            "keyboard": [
                [button.to_dict() for button in row]
                for row in self._keyboard
            ],
            "is_persistent": self._is_persistent,
            "resize_keyboard": self._resize_keyboard,
            "one_time_keyboard": self._one_time_keyboard,
            "input_field_placeholder": self._input_field_placeholder,
            "selective": self._selective,
        }
