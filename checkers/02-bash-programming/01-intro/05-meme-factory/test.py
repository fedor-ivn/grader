import subprocess
import os
import termios
import difflib


# Define the command to run
cmd = "solution.sh"


class InteractiveSession:
    def __init__(self, path, args=[]):
        self.master, self.slave = os.openpty()
        old = termios.tcgetattr(self.slave)
        old[3] &= ~termios.ECHO
        termios.tcsetattr(
            self.slave, termios.TCSADRAIN, old
        )

        self.child = subprocess.Popen(
            ["bash", path, *args],
            stdout=self.slave,
            stdin=self.slave,
            stderr=self.slave,
            text=True,
        )

    def health_check(self):
        pass

    def enter_line(self, line: str, add_newline=True):
        if add_newline:
            line += "\n"
        os.write(self.master, line.encode())

    def expect_output(self, expected_output: str):
        while True:
            line = os.read(self.master, 100).decode("utf-8")
            print(line)
            if line == expected_output:
                print("win")
                return True

            return False

    def terminate(self):
        self.child.terminate("123")


session = InteractiveSession("solution.sh")
session.enter_line("Введите что-нибудь")
session.expect_output("Введите что-нибудь")
session.expect_output("Введите что-нибудь\r\n")
