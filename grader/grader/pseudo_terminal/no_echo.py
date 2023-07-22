from grader.pseudo_terminal.pseudo_terminal import (
    PseudoTerminal,
)
import termios


class NoEchoPseudoTerminal(PseudoTerminal):
    """
    Creates an instance of the terminal which will not echo
    its stdin into the stdout
    """

    def __init__(
        self, pseudo_terminal: PseudoTerminal
    ) -> None:
        """
        Initializes a new instance of SequentialCriteria

        Attributes:
            pseudo_terminal (PseudoTerminal): the pseudo instance of the terminal
        """
        self._pseudo_terminal = pseudo_terminal

    def create_fds(self) -> tuple[int, int]:
        """
        Creates abd returns the fds of the pseudo terminal without echo
        """
        master, slave = self._pseudo_terminal.create_fds()
        old = termios.tcgetattr(slave)
        old[3] &= ~termios.ECHO
        termios.tcsetattr(slave, termios.TCSADRAIN, old)
        return master, slave
