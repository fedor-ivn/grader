import os
from abc import ABC, abstractmethod
from typing import TypeVar
import warnings
from bot.token import Token
from methods.method import Method
from state import State
from uri.method_uri import MethodURI
from uri.telegram_api_uri import TelegramApiURI
from uri.uri import URI


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
        """
        todo: need to clarify if we can do such call chains
            bot -> state -> bot
        """
        return method.call(self)

    def start(self, state: State) -> None:
        """
        todo: need to clarify if we can do such call chains
            bot -> state -> bot
        """
        state.start(self)
