from typing import Any
from arguments.argument import (
    MethodArgument,
)
from more_itertools import flatten


class MethodArguments(MethodArgument):
    def __init__(
        self, methods: list[MethodArgument] = []
    ) -> None:
        self.methods = methods

    def to_dict(self) -> dict[str, Any]:
        return dict(
            flatten(
                [
                    method.to_dict().items()
                    for method in self.methods
                ]
            )
        )
