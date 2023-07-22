from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from uri.uri import URI

T = TypeVar("T")


class Method(ABC, Generic[T]):
    @abstractmethod
    def call(self, uri: URI) -> T:
        pass
