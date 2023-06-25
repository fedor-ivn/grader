from typing import Any
from arguments.argument import (
    MethodArgument,
)


class EmptyArgument(MethodArgument):
    def to_dict(self) -> dict[str, Any]:
        return {}
