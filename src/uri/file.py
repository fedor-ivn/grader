from uri.telegram_api_uri import TelegramApiURI
from uri.uri import URI
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class DocumentURI(URI):
    def __init__(
        self,
        file_path: str,
        bot: URI,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._file_path = file_path
        self._bot = bot
        self._log = log

    def construct_uri(self) -> str:
        self._log.info(
            f"Constructing URI for file {self._file_path}"
        )
        return (
            f"{self._bot.construct_uri()}{self._file_path}"
        )
