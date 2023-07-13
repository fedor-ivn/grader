from subprocess import Popen
from grader.pseudo_terminal.simple import (
    SimplePseudoTerminal,
)
from grader.pseudo_terminal.no_echo import (
    NoEchoPseudoTerminal,
)
from grader.ibash.session import IBashSession


class IBash:
    """
    The class which creates the session for the provided script
    """

    def __init__(self, path: str):
        """
        Create a new instance of IBash

        Attributes:
            path (str): the path to the script
        """
        self._path = path
        self._pty = NoEchoPseudoTerminal(SimplePseudoTerminal())
        self._args: list[str] = []

    def start_session(self) -> IBashSession:
        """
        Returns a new instance of the IBashSession, which will then be used
        to interact with the script and grade it
        """
        master, slave = self._pty.create_fds()
        process = Popen(
            ["/bin/bash", "-c", self._path, *self._args],
            stdout=slave,
            stdin=slave,
            stderr=slave,
            text=True,
        )
        return IBashSession(process, master)
