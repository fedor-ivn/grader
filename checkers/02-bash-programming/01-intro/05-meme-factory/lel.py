from abc import ABC, abstractmethod
import os
import errno
import pickle
from threading import Thread
from typing import Any
import subprocess

import args_proxy


class MockExecutablePipe:
    def __init__(self, name: str):
        self.name: str = name

    def create(self) -> None:
        try:
            if os.path.exists(self.name):
                os.remove(self.name)
            os.mkfifo(self.name)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise

    def read(self, args: list[str]) -> Any:
        with open(self.name, "rb") as pipe:
            pickled_args: list[str] = pickle.load(pipe)
            args += pickled_args


class MockExecutable:
    def __init__(self, name: str, pipe: MockExecutablePipe):
        self.name = name
        self.pipe = pipe

    def get_script(self) -> str:
        return args_proxy.script_template.format(
            pipe_name=self.pipe.name
        )

    def create(self) -> None:
        with open(self.name, "w") as executable:
            executable.write(self.get_script())

        os.chmod(self.name, 0o755)

        env_path_list: list[str] = os.environ["PATH"].split(
            os.pathsep
        )
        if self.name not in env_path_list:
            os.environ["PATH"] = os.pathsep.join(
                [os.getcwd()] + env_path_list
            )

    def get_args(self) -> list[str]:
        args: list[str] = []
        t = Thread(target=self.pipe.read, args=args)
        t.start()
        t.join()
        return args


class Criterion(ABC):
    """
    Interface for all criteria
    """

    @abstractmethod
    def check(self) -> bool:
        ...


class IOCriterion:
    pass


class ArgumentsCriterion:
    def __init__(self, arg: object, mock_utility: object):
        self.args: object = arg
        self.mock_utility: object = mock_utility

    def check(self) -> None:
        pass


def test() -> None:
    executable = MockExecutable(
        "convert", MockExecutablePipe("example")
    )
    executable.create()
    executable.pipe.create()

    args: list[str] = []
    t = Thread(target=executable.pipe.read, args=[args])
    t.start()

    child = subprocess.Popen(
        ["bash", "temp-reference-solution.sh", *args],
        # stdout=subprocess.PIPE,
        # stdin=subprocess.PIPE,
        # stderr=subprocess.PIPE,
        text=True,
    )

    # try:
    t.join(timeout=10)
    print(args)


test()
