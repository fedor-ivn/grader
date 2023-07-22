from arguments.keyboard.button import Button


class ListToButtons:
    def __init__(self, string_list: list[str]):
        self._string_list = string_list

    def buttons_list(self) -> list[Button]:
        buttons_list = []

        for entry in self._string_list:
            buttons_list.append(Button(entry))

        return buttons_list
