from typing import Any
from arguments.argument import MethodArgument


class Button(MethodArgument):
    """
    todo:
        [] Add suppport for...
            [] request_user
            [] request_chat
            [] request_contact
            [] request_location
            [] request_poll
            [] request_game
    """

    def __init__(self, text: str) -> None:
        self.text = text

    def to_dict(self) -> dict[str, Any]:
        return {
            "text": self.text,
        }
