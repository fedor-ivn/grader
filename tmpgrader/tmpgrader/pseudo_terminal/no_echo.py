from pseudo_terminal import PseudoTerminal
import termios


class NoEchoPseudoTerminal(PseudoTerminal):
    def __init__(self, pseudo_terminal) -> None:
        self._pseudo_terminal = pseudo_terminal

    def create_fds(self):
        master, slave = self._pseudo_terminal.create_fds()
        old = termios.tcgetattr(slave)
        old[3] &= ~termios.ECHO
        termios.tcsetattr(slave, termios.TCSADRAIN, old)
        return master, slave
