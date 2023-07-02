from grader.pseudo_terminal.pseudo_terminal import (
    PseudoTerminal,
)
import os
from typing import Tuple


class SimplePseudoTerminal(PseudoTerminal):
    def __init__(self) -> None:
        pass

    def create_fds(self) -> Tuple[int, int]:
        return os.openpty()
