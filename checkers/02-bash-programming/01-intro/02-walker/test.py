from abc import ABC, abstractmethod
import errno
import os
import pickle
import termios
from subprocess import Popen
from threading import Thread
from typing import Any

import args_proxy


class PseudoTerminal(ABC):
    @abstractmethod
    def create_fds(self):
        ...


class SimplePseudoTerminal(PseudoTerminal):
    def __init__(self):
        pass

    def create_fds(self):
        return os.openpty()


class NoEchoPseudoTerminal(PseudoTerminal):
    def __init__(self, pseudo_terminal) -> None:
        self._pseudo_terminal = pseudo_terminal

    def create_fds(self):
        master, slave = self._pseudo_terminal.create_fds()
        old = termios.tcgetattr(slave)
        old[3] &= ~termios.ECHO
        termios.tcsetattr(slave, termios.TCSADRAIN, old)
        return master, slave


class IBashSession:
    def __init__(self, process: Popen, master):
        self._process = process
        self._master = master

    def enter_line(
        self, line: str, add_newline: bool = True
    ):
        if add_newline:
            line += "\n"
        os.write(self._master, line.encode())

    def expect_output(self, expected_output: str):
        line = os.read(self._master, 100)
        return line == expected_output.encode()

    def prompt(self, expected_prompt: str, enter: str):
        ok = self.expect_output(expected_prompt)
        self.enter_line(enter)
        return ok


class IBash:
    def __init__(self, path: str):
        self._path = path
        self._pty = NoEchoPseudoTerminal(
            SimplePseudoTerminal()
        )
        # todo: govnokod
        self._args = []

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


class Criterion(ABC):
    @abstractmethod
    def test(self, solution: str):
        pass


class PipeSession:
    def __init__(self, args, thread: Thread, timeout: int):
        self.args = args
        self.thread = thread
        self.timeout = timeout

    def start_session(self):
        self.thread.start()

    def collect_args(self):
        self.thread.join(timeout=self.timeout)
        if self.thread.is_alive():
            raise TimeoutError
        return self.args


class MockExecutablePipe:
    def __init__(self, name: str):
        self.name: str = name

    def create(self) -> PipeSession:
        try:
            if os.path.exists(self.name):
                os.remove(self.name)
            os.mkfifo(self.name)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise
        args = []
        # todo: timeout const govnokod
        return PipeSession(
            args, Thread(target=self.read, args=[args]), 1
        )

    def read(self, args: list[str]) -> None:
        with open(self.name, "rb") as pipe:
            pickled_args: list[str] = pickle.load(pipe)
            args += pickled_args


class MockExecutable:
    def __init__(self, name: str, pipes_path: str):
        self.name = name
        self.pipe_path = f"{pipes_path}/{name}"
        self.pipe = MockExecutablePipe(self.pipe_path)

    def create(self) -> PipeSession:
        with open(self.name, "w") as executable:
            executable.write(
                args_proxy.script_template.format(
                    pipe_path=self.pipe_path
                )
            )

        os.chmod(self.name, 0o755)
        env_path_list: list[str] = os.environ["PATH"].split(
            os.pathsep
        )

        cwd = os.getcwd()
        if cwd not in env_path_list:
            os.environ["PATH"] = os.pathsep.join(
                [cwd] + env_path_list
            )
        return self.pipe.create()


class OutputCriterion(Criterion):
    def __init__(self, expected_output: str):
        self._expected_output = expected_output

    def test(self, solution: IBashSession):
        is_expected = solution.expect_output(
            self._expected_output
        )
        print(is_expected)
        return is_expected


class PromptCriterion(Criterion):
    def __init__(self, expected_prompt: str, enter: str):
        self._expected_prompt = expected_prompt
        self._enter = enter

    def test(self, solution: IBashSession):
        is_expected = solution.prompt(
            self._expected_prompt, self._enter
        )
        print(is_expected)
        return is_expected


class ArgumentsCriterion(Criterion):
    def __init__(self, mock_executable: MockExecutable):
        self._mock_executable = mock_executable
        # todo: govnokod
        self._pipe_session = self._mock_executable.create()
        self._pipe_session.start_session()

    def test(self, solution: IBashSession):
        collected_args = self._pipe_session.collect_args()
        print(collected_args)
        return True


class SequentialCriteria(Criterion):
    def __init__(self, criteria: list[Criterion]):
        self._criteria = criteria

    def test(self, solution: IBashSession):
        for criterion in self._criteria:
            result = criterion.test(solution)
            if not result:
                return False
        return True


class Criteria:
    def __init__(self, criteria: list[Criterion]):
        self._criteria = criteria

    def test(self, solution: IBashSession):
        return [
            criterion.test(solution)
            for criterion in self._criteria
        ]


class MemeFactoryTest:
    def __init__(self):
        convert_mock = MockExecutable("convert", "pipes")
        pipe_session = convert_mock.create()
        self._criteria = SequentialCriteria(
            [
                SequentialCriteria(
                    [
                        PromptCriterion(
                            expected_prompt="Подпись к мему: ",
                            enter="четыре",
                        ),
                        PromptCriterion(
                            expected_prompt="Название файла: ",
                            enter="six-four.jpg",
                        ),
                    ]
                ),
                SequentialCriteria(
                    [
                        ArgumentsCriterion(convert_mock),
                    ]
                ),
                OutputCriterion(
                    "Мем сохранён!\r\n"
                )
            ]
        )

    def test(self, solution: IBash):
        self._criteria.test(solution.start_session())


MemeFactoryTest().test(IBash("solution.sh"))
