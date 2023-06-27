from abc import ABC, abstractmethod
import json
from typing import Any, Generic, TypeVar


class RequestContent(ABC):
    @abstractmethod
    def data(self) -> bytes:
        ...

    @abstractmethod
    def content_type(self) -> str:
        ...


class JsonRequestContent(RequestContent):
    def __init__(self, content: dict[str, Any]) -> None:
        self._content = content

    # def get_request_kwargs(
    #     self,
    # ) -> dict[str, str | dict[str, str]]:
    #     return {
    #         "data": json.dumps(self._content),
    #         "headers": {"Content-Type": "application/json"},
    #     }

    def data(self) -> bytes:
        return json.dumps(self._content).encode("utf-8")

    def content_type(self) -> str:
        return "application/json"


class EmptyRequestContent(RequestContent):
    def data(self) -> bytes:
        return b""

    def content_type(self) -> str:
        return "application/json"
