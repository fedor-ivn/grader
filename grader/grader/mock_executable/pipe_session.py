from threading import Thread


class PipeSession:
    def __init__(
        self, args: list[str], thread: Thread, timeout: int
    ) -> None:
        self.args = args
        self.thread = thread
        self.timeout = timeout

    def start_session(self) -> None:
        self.thread.start()

    def collect_args(self) -> list[str]:
        self.thread.join(timeout=self.timeout)
        if self.thread.is_alive():
            raise TimeoutError
        return self.args
