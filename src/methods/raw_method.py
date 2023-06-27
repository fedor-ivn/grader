import json
from typing import Any, Generic, TypeVar
import requests

from content import RequestContent
from exceptions import (
    ApiMethodException,
    NetworkException,
    OutOfServiceException,
    UnexpectedResponseException,
)

from methods.method import Method
from uri.uri import URI
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class RawMethod(Method[Any]):
    def __init__(
        self,
        content: RequestContent,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._content = content
        self.log = log

    def call(self, method_uri: URI) -> Any:
        # print(method_uri.construct_uri())
        self.log.info(
            f"Calling {method_uri.construct_uri()}"
        )
        try:
            response = requests.post(
                method_uri.construct_uri(),
                data=self._content.data(),
                headers={
                    "Content-Type": self._content.content_type()
                },
            )
            self.log.info(
                f"Response status code: {response.status_code}"
            )
        except KeyError:
            self.log.error("Network error")
            raise NetworkException

        raw_json_response = response.text
        if raw_json_response.startswith("<"):
            raise OutOfServiceException

        # print(raw_json_response)
        json_response = json.loads(raw_json_response)

        match json_response:
            case {"ok": True, "result": result}:
                self.log.info("Response is ok")
                return result
            case {
                "ok": False,
                "description": str(description),
                "error_code": int(error_code),
            }:
                self.log.error("Response is not ok")
                raise ApiMethodException(
                    description,
                    error_code,
                )
            case _:
                self.log.error("Unexpected response")
                raise UnexpectedResponseException
