from subprocess import Popen
import os
import fcntl
import errno
import time


class IBashSession:
    """ """

    def __init__(self, process: Popen, master: int) -> None:
        self._process = process
        self._master = master

    def enter_line(self, line: str, add_newline: bool = True) -> None:
        if add_newline:
            line += "\n"
        os.write(self._master, line.encode())

    def expect_output(self, expected_output: str) -> bool:
        line = b""

        flags = fcntl.fcntl(self._master, fcntl.F_GETFL)
        fcntl.fcntl(self._master, fcntl.F_SETFL, flags | os.O_NONBLOCK)

        start_time = time.time()
        while True:
            try:
                line += os.read(self._master, 100)
            except OSError as e:
                if e.errno != errno.EAGAIN:
                    raise

            elapsed_time = time.time() - start_time
            if elapsed_time >= 1:
                break

            time.sleep(0.1)

        flags = fcntl.fcntl(self._master, fcntl.F_GETFL)
        fcntl.fcntl(self._master, fcntl.F_SETFL, flags & ~os.O_NONBLOCK)
        return line == expected_output.encode()

    def prompt(self, expected_prompt: str, enter: str) -> bool:
        ok = self.expect_output(expected_prompt)
        self.enter_line(enter)
        return ok

    def check_error(self) -> int:
        return self._process.wait()
