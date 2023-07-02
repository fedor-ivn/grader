from subprocess import Popen
from grader.pseudo_terminal.simple import (
    SimplePseudoTerminal,
)
from grader.pseudo_terminal.no_echo import (
    NoEchoPseudoTerminal,
)
from grader.ibash.session import IBashSession


class IBash:
    def __init__(self, path: str):
        self._path = path
        self._pty = NoEchoPseudoTerminal(
            SimplePseudoTerminal()
        )
        # todo: govnokod
        self._args: list[str] = []

    def start_session(self) -> IBashSession:
        master, slave = self._pty.create_fds()
        process = Popen(
            ["bash", self._path, *self._args],
            stdout=slave,
            stdin=slave,
            stderr=slave,
            text=True,
        )
        return IBashSession(process, master)
