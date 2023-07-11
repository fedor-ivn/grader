from eobot.arguments.argument import (
    MethodArgument,
)
from typing import Any

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class BotCommand(MethodArgument):
    def __init__(
        self,
        command: str,
        description: str,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._command = command
        self._description = description
        self._log = log

    def to_dict(self) -> dict[str, Any]:
        self._log.debug(
            f"Converting BotCommand to dict {self._command}"
        )
        return {
            "command": self._command,
            "description": self._description,
        }
