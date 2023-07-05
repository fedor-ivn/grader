from abc import ABC, abstractmethod
from typing import Any, TypeVar, Generic
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


T = TypeVar("T")


class RawType(ABC, Generic[T]):
    def __init__(
        self,
        raw_object: dict[str, Any],
        log: AbstractLog = NoLog(),
    ) -> None:
        self._raw = raw_object
        self._log = log

    @abstractmethod
    def parse(self) -> T:
        ...
