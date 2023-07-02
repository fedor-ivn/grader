from subprocess import Popen
import os


class IBashSession:
    def __init__(self, process: Popen, master: int) -> None:
        self._process = process
        self._master = master

    def enter_line(
        self, line: str, add_newline: bool = True
    ) -> None:
        if add_newline:
            line += "\n"
        os.write(self._master, line.encode())

    def expect_output(self, expected_output: str) -> bool:
        line = os.read(self._master, 100)
        return line == expected_output.encode()

    def prompt(
        self, expected_prompt: str, enter: str
    ) -> bool:
        ok = self.expect_output(expected_prompt)
        self.enter_line(enter)
        return ok
