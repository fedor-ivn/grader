import json
from typing import Any
import requests

from content import Content
from exceptions import (
    ApiMethodException,
    NetworkException,
    OutOfServiceException,
    UnexpectedResponseException,
)

from methods.method import Method
from uri.method_uri import MethodURI


class RawMethod(Method[Any]):
    def __init__(
        self, method_uri: MethodURI, content
    ) -> None:
        self._method_uri = method_uri
        self._content = content

    def call(self) -> Any:
        print(self._method_uri.construct_uri())
        try:
            response = requests.post(
                self._method_uri.construct_uri(),
                **self._content.get_request_args(),
            )
        except KeyError:
            raise NetworkException

        raw_json_response = response.text
        if raw_json_response.startswith("<"):
            raise OutOfServiceException

        print(raw_json_response)
        json_response = json.loads(raw_json_response)

        match json_response:
            case {"ok": True, "result": result}:
                return result
            case {
                "ok": False,
                "description": str(description),
                "error_code": int(error_code),
            }:
                raise ApiMethodException(
                    json_response["description"],
                    json_response["error_code"],
                )
            case _:
                raise UnexpectedResponseException
import json
from typing import Any
import requests

from content import Content
from exceptions import (
    ApiMethodException,
    NetworkException,
    OutOfServiceException,
    UnexpectedResponseException,
)

from methods.method import Method
from uri.method_uri import MethodURI


class RawMethod(Method[Any]):
    def __init__(
        self, method_uri: MethodURI, content: Content
    ) -> None:
        self._method_uri = method_uri
        self._content = content

    def call(self) -> Any:
        # print(self._method_uri.construct_uri())
        try:
            response = requests.post(
                self._method_uri.construct_uri(),
                **self._content.get_request_args(),
            )
        except KeyError:
            raise NetworkException

        raw_json_response = response.text
        if raw_json_response.startswith("<"):
            raise OutOfServiceException

        # print(raw_json_response)
        json_response = json.loads(raw_json_response)

        match json_response:
            case {"ok": True, "result": result}:
                return result
            case {
                "ok": False,
                "description": str(description),
                "error_code": int(error_code),
            }:
                raise ApiMethodException(
                    json_response["description"],
                    json_response["error_code"],
                )
            case _:
                raise UnexpectedResponseException
