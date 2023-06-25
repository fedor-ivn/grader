from threading import Thread


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
