from abc import ABC, abstractmethod
from typing import Any


class AbstractMethodArgument(ABC):
    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        ...
