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
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


T = TypeVar("T")


class Bot(URI):
    def __init__(
        self,
        token: Token,
        api_uri: URI = TelegramApiURI(),
        log: AbstractLog = NoLog(),
    ) -> None:
        self._token = token
        self._api_uri = api_uri
        self._log = log

    def construct_uri(self) -> str:
        self._log.debug(
            f"Bot: {self._token.token()}"
            f"API URI: {self._api_uri.construct_uri()}"
        )
        return f"{self._api_uri.construct_uri()}bot{self._token.token()}/"

    def call_method(self, method: Method[T]) -> T:
        """
        todo: need to clarify if we can do such call chains
            bot -> state -> bot
        """
        self._log.debug(
            f"Bot: {self._token.token()}"
            f"URI: {self._api_uri.construct_uri()}"
        )
        return method.call(self)

    def start(self, state: State) -> None:
        """
        todo: need to clarify if we can do such call chains
            bot -> state -> bot
        """
        self._log.info("Bot.start()")
        state.start(self)
