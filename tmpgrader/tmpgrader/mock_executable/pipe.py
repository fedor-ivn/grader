from tmpgrader.mock_executable.pipe_session import (
    PipeSession,
)
import os
from threading import Thread
import errno
import pickle


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
        args = list[str]
        # todo: timeout const govnokod
        return PipeSession(
            args, Thread(target=self.read, args=[args]), 1
        )

    def read(self, args: list[str]) -> None:
        with open(self.name, "rb") as pipe:
            pickled_args: list[str] = pickle.load(pipe)
            args += pickled_args
