from arguments.keyboard.button import Button
from arguments.keyboard.keyboard import ReplyKeyboard


class CreateKeyboard:
    def __init__(self, buttons_list: list[Button]) -> None:
        self._buttons_list = buttons_list

    def create(self) -> ReplyKeyboard:
        splitted_buttons_list = [
            self._buttons_list[i : i + 2]
            for i in range(0, len(self._buttons_list), 2)
        ]
        return ReplyKeyboard(splitted_buttons_list)
