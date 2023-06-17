from abc import ABC, abstractmethod

import os
import errno
import pickle
import shutil
from threading import Thread
import args_proxy


FIFO = "meme-factory-named-pipe"
print("Opening FIFO...")
with open(FIFO) as fifo:
    print("FIFO opened")
    while True:
        data = fifo.read()
        if len(data) == 0:
            print("Writer closed")
            break
        print('Read: "{0}"'.format(data))


class MockUtilityPipe:
    def __init__(self, name):
        self.name = name

    def create(self):
        try:
            if not os.path.exists(self.name):
                os.mkfifo(self.name)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise

    def read(self):
        self.create()
        with open(self.name, "rb") as pipe:
            args = pickle.load(pipe)
        return args


class MockExecutable:
    def __init__(self, name, pipe):
        self.name = name
        self.pipe = pipe

    def get_script(self):
        return args_proxy.script_template.format(
            pipe_name=self.pipe.name
        )

    def create(self):
        with open("convert", "w") as executable:
            executable.write(self.get_script())

        os.chmod(self.name, 0o755)

        env_path_list = os.environ["PATH"].split(os.pathsep)
        if self.name not in env_path_list:
            os.environ["PATH"] = os.pathsep.join(
                env_path_list + [self.name]
            )


class MockUtility:
    def __init__(self, executable):
        self.executable = executable

    def get_args(self):
        self.executable.create()
        Thread(target=self.pipe.read).start()


class Criterion(ABC):
    """
    Interface for all criteria
    """

    @abstractmethod
    def check() -> bool:
        ...


class IOCriterion:
    pass


class ArgumentsCriterion:
    def __init__(self, arg, mock_utility):
        self.args = arg
        self.mock_utility

    def check(self):
        pass


def test():
    MockUtility("convert").create_mock_executable()
