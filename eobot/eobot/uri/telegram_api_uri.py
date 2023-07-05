from eobot.uri.uri import URI
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class TelegramApiURI(URI):
    def __init__(
        self,
        api_uri: str = "https://api.telegram.org/",
        log: AbstractLog = NoLog(),
    ) -> None:
        self._api_uri = api_uri
        self._log = log

    def construct_uri(self) -> str:
        self._log.info("Constructing URI")
        return self._api_uri
