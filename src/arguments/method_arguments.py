from typing import Any
from arguments.argument import (
    MethodArgument,
)
from more_itertools import flatten

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class MethodArguments(MethodArgument):
    def __init__(
        self,
        methods: list[MethodArgument] = [],
        log: AbstractLog = NoLog(),
    ) -> None:
        self.methods = methods
        self.log = log

    def to_dict(self) -> dict[str, Any]:
        self.log.debug("MethodArguments.to_dict()")
        return dict(
            flatten(
                [
                    method.to_dict().items()
                    for method in self.methods
                ]
            )
        )
