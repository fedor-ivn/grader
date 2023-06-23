from abc import ABC, abstractmethod
import json
from typing import Any, Generic, TypeVar


T = TypeVar("T")


class Content(ABC, Generic[T]):
    @abstractmethod
    def get_request_args(self) -> T:
        ...


class JsonContent(Content[dict[str, str | dict[str, str]]]):
    def __init__(self, content: Any) -> None:
        self._content = content

    def get_request_args(
        self,
    ) -> dict[str, str | dict[str, str]]:
        return {
            "data": json.dumps(self._content),
            "headers": {"Content-Type": "application/json"},
        }


class EmptyContent(Content[dict[Any, Any]]):
    def get_request_args(self) -> dict[Any, Any]:
        return {}
