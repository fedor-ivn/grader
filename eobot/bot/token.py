from abc import ABC, abstractmethod
import os
import warnings

from dotenv.main import DotEnv

from exceptions import TokenNotFoundError

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class Token(ABC):
    @abstractmethod
    def token(self) -> str:
        pass


class InlineToken(Token):
    def __init__(
        self, token: str, log: AbstractLog = NoLog()
    ) -> None:
        self._token = token
        self._log = log

    def token(self) -> str:
        warnings.warn(
            (
                "Harcoded tokens are not secure! "
                "Use `EnvironmentToken` instead."
            ),
            UserWarning,
        )
        self._log.info("Using hardcoded token.")
        self._log.warning(
            "Harcoded tokens are not secure! "
            "Use `EnvironmentToken` instead."
        )
        return self._token


class EnvironmentToken(Token):
    def __init__(
        self, env_var: str, log: AbstractLog = NoLog()
    ) -> None:
        self._env_var = env_var
        self._log = log

    def token(self) -> str:
        self._log.info("Environment token found.")
        try:
            return os.environ[self._env_var]
        except KeyError:
            self._log.error(
                f"Environment variable {self._env_var} is not set."
            )
            raise TokenNotFoundError(
                f"Environment variable {self._env_var} is not set."
            )


class DotenvToken(Token):
    def __init__(
        self,
        env_var: str,
        dotenv: DotEnv,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._env_var = env_var
        self._dotenv = dotenv
        self._log = log

    def token(self) -> str:
        try:
            dotenv_dict = self._dotenv.dict()
            self._log.info("Dotenv token found.")
            return dotenv_dict[self._env_var]  # type: ignore
        except KeyError:
            self._log.error(
                f"Environment variable {self._env_var} is not found in dotenv."
            )
            raise TokenNotFoundError(
                f"Environment variable {self._env_var} is not found in dotenv."
            )
