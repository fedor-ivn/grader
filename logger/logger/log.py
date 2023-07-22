import logging
from logging import Logger
from logger.abstract_log import AbstractLog


class LogConfig:
    def __init__(
        self, level: int, format: str, datefmt: str
    ) -> None:
        self._level = level
        self._format = format
        self._datefmt = datefmt

    def configure(self) -> AbstractLog:
        logging.basicConfig(
            level=self._level,
            format=self._format,
            datefmt=self._datefmt,
        )
        logger = logging.getLogger(__name__)
        return Log(logger=logger)


class Log(AbstractLog):
    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def debug(self, message: str) -> None:
        self.logger.debug(message)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def critical(self, message: str) -> None:
        self.logger.critical(message)
