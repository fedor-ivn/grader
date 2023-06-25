import os
from abc import ABC, abstractmethod
from typing import TypeVar
import warnings
from methods.method import Method
from uri.method_uri import MethodURI
from uri.telegram_api_uri import TelegramApiURI
from uri.uri import URI


class Token(ABC):
    @abstractmethod
    def token(self) -> str:
        pass


class InlineToken(Token):
    def __init__(self, token: str) -> None:
        self._token = token

    def token(self) -> str:
        warnings.warn(
            (
                "Harcoded tokens are not secure! "
                "Use `EnvironmentToken` instead."
            ),
            UserWarning,
        )
        return self._token


class EnvironmentToken(Token):
    def __init__(self, env_var: str) -> None:
        self._env_var = env_var

    def token(self) -> str:
        try:
            return os.environ[self._env_var]
        except KeyError:
            raise KeyError(
                f"Environment variable {self._env_var} is not set."
            )


T = TypeVar("T")


class Bot(URI):
    def __init__(
        self, token: Token, api_uri: URI = TelegramApiURI()
    ) -> None:
        self._token = token
        self._api_uri = api_uri

    def construct_uri(self) -> str:
        return f"{self._api_uri.construct_uri()}bot{self._token.token()}/"

    def call_method(self, method: Method[T]) -> T:
        return method.call(self)
