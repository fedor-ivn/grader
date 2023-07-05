from eobot.arguments.argument import MethodArgument

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class AbstractThreadId(MethodArgument):
    pass


class NoThreadId(AbstractThreadId):
    def to_dict(self) -> dict[str, int]:
        return {}


class ThreadId(AbstractThreadId):
    def __init__(
        self, thread_id: int, log: AbstractLog = NoLog()
    ) -> None:
        self._thread_id = thread_id
        self._log = log

    def to_dict(self) -> dict[str, int]:
        self._log.debug(f"ThreadId: {self._thread_id}")
        return {
            "thread_id": self._thread_id,
        }
