from abc import ABC, abstractmethod
from typing import Any


class MethodArgument(ABC):
    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        ...
