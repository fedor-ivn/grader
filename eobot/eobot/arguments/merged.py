from typing import Any
from eobot.arguments.argument import MethodArgument

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class MergedArgument(MethodArgument):
    def __init__(
        self,
        initial: MethodArgument,
        update: MethodArgument,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._initial = initial
        self._update = update
        self._log = log

    def to_dict(self) -> dict[str, Any]:
        self._log.info(
            "Merging arguments"
            f" {self._initial.to_dict()}"
            f" {self._update.to_dict()}"
        )
        return (
            self._initial.to_dict() | self._update.to_dict()
        )
