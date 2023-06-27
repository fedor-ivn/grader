from uri.uri import URI
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class MethodURI(URI):
    def __init__(
        self,
        method: str,
        bot: URI,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._method = method
        self._bot = bot
        self.log = log

    def construct_uri(self) -> str:
        self.log.info(
            f"Constructing URI for method {self._method}"
        )
        return f"{self._bot.construct_uri()}{self._method}"
