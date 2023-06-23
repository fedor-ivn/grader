from abc import ABC, abstractmethod


class URI(ABC):
    @abstractmethod
    def construct_uri(self) -> str:
        ...
