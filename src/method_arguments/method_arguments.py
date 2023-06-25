from typing import Any
from method_arguments.method_argument import (
    AbstractMethodArgument,
)
from more_itertools import flatten


class MethodArguments(AbstractMethodArgument):
    def __init__(
        self, methods: list[AbstractMethodArgument] = []
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
