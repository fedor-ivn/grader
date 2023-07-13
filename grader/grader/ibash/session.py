from subprocess import Popen
import os
import fcntl
import errno
import time


class IBashSession:
    """
    The class which is used to interact with the script
    """

    def __init__(self, process: Popen, master: int) -> None:
        """
        Creates a new IBashSession instance.

        Attributes:
            process (Popen): The created subprocess for the script
            master (int): the input/output channel of the created subprocess
        """
        self._process = process
        self._master = master

    def enter_line(self, line: str, add_newline: bool = True) -> None:
        """
        Enters the line into the script

        Args:
        line (str): the line which will be entered
        add_newline (bool): whether a '\n' symbol should be added in the end
        """
        if add_newline:
            line += "\n"
        os.write(self._master, line.encode())

    def expect_output(self, expected_output: str) -> bool:
        """
        Reads the buffer, waiting for the output of the script

        Args:
            expected_output (str): the string that is expected to be received from stdout
        """
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
        """
        Reads the buffer and writes the string into stdin

        Args:
            expected_prompt (str): the string that is expected to be received from stdout
            enter (str): the string that will be entered in stdin
        """
        ok = self.expect_output(expected_prompt)
        self.enter_line(enter)
        return ok

    def check_error(self) -> int:
        """
        Checks the exit code of the script
        """
        return self._process.wait()
