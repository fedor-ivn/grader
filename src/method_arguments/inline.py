from method_arguments.method_argument import (
    AbstractMethodArgument,
)
from typing import Any


class InlineMethodArgument(AbstractMethodArgument):
    def __init__(self, key: str, value: Any) -> None:
        self._key = key
        self._value = value

    def to_dict(self) -> dict[str, Any]:
        return {self._key: self._value}
