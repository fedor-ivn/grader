from abc import ABC, abstractmethod
import json
from typing import Any, Generic, TypeVar
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class RequestContent(ABC):
    @abstractmethod
    def data(self) -> bytes:
        ...

    @abstractmethod
    def content_type(self) -> str:
        ...


class JsonRequestContent(RequestContent):
    def __init__(
        self,
        content: dict[str, Any],
        log: AbstractLog = NoLog(),
    ) -> None:
        self._content = content
        self.log = log

    # def get_request_kwargs(
    #     self,
    # ) -> dict[str, str | dict[str, str]]:
    #     return {
    #         "data": json.dumps(self._content),
    #         "headers": {"Content-Type": "application/json"},
    #     }

    def data(self) -> bytes:
        self.log.info("JsonRequestContent.data()")
        return json.dumps(self._content).encode("utf-8")

    def content_type(self) -> str:
        self.log.info("JsonRequestContent.content_type()")
        return "application/json"


class EmptyRequestContent(RequestContent):
    def data(self) -> bytes:
        return b""

    def content_type(self) -> str:
        return "application/json"
