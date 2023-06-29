from tmpgrader.pseudo_terminal.pseudo_terminal import (
    PseudoTerminal,
)
import os


class SimplePseudoTerminal(PseudoTerminal):
    def __init__(self):
        pass

    def create_fds(self):
        return os.openpty()
