from typing import Any
from method_arguments.method_argument import (
    AbstractMethodArgument,
)


class EmptyArgument(AbstractMethodArgument):
    def to_dict(self) -> dict[str, Any]:
        return {}
