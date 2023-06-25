from abc import ABC, abstractmethod
import json
from typing import Any, Generic, TypeVar


T = TypeVar("T")


class RequestContent(ABC, Generic[T]):
    @abstractmethod
    def get_request_kwargs(self) -> T:
        ...


class JsonRequestContent(
    RequestContent[dict[str, str | dict[str, str]]]
):
    def __init__(self, content: dict[str, Any]) -> None:
        self._content = content

    def get_request_kwargs(
        self,
    ) -> dict[str, str | dict[str, str]]:
        return {
            "data": json.dumps(self._content),
            "headers": {"Content-Type": "application/json"},
        }


class EmptyRequestContent(RequestContent[dict[Any, Any]]):
    def get_request_kwargs(self) -> dict[Any, Any]:
        return {}
