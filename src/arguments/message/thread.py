from arguments.argument import MethodArgument


class AbstractThreadId(MethodArgument):
    pass


class NoThreadId(AbstractThreadId):
    def to_dict(self) -> dict[str, int]:
        return {}


class ThreadId(AbstractThreadId):
    def __init__(self, thread_id: int) -> None:
        self._thread_id = thread_id

    def to_dict(self) -> dict[str, int]:
        return {
            "thread_id": self._thread_id,
        }
