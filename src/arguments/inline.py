from arguments.argument import (
    MethodArgument,
)
from typing import Any

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class InlineArgument(MethodArgument):
    def __init__(
        self,
        key: str,
        value: Any,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._key = key
        self._value = value
        self.log = log

    def to_dict(self) -> dict[str, Any]:
        self.log.debug(
            f"InlineArgument: {self._key}={self._value}"
        )
        return {self._key: self._value}
