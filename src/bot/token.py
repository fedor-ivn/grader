from abc import ABC, abstractmethod
import os
import warnings

from dotenv.main import DotEnv

from exceptions import TokenNotFoundError


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
            raise TokenNotFoundError(
                f"Environment variable {self._env_var} is not set."
            )


class DotenvToken(Token):
    def __init__(
        self, env_var: str, dotenv: DotEnv
    ) -> None:
        self._env_var = env_var
        self._dotenv = dotenv

    def token(self) -> str:
        try:
            dotenv_dict = self._dotenv.dict()
            return dotenv_dict[self._env_var]  # type: ignore
        except KeyError:
            raise TokenNotFoundError(
                f"Environment variable {self._env_var} is not found in dotenv."
            )
