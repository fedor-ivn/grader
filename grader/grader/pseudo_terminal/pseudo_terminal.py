from abc import ABC, abstractmethod


class PseudoTerminal(ABC):
    @abstractmethod
    def create_fds(self) -> tuple[int, int]:
        ...
