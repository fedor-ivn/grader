import logging
from logger.abstract_log import AbstractLog

class Log(AbstractLog):
    def __init__(self) -> None:
        logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
    
    def debug(self, message: str) -> None:
        logging.debug(message)

    def info(self, message: str) -> None:
        logging.info(message)

    def warning(self, message: str) -> None:
        logging.warning(message)

    def error(self, message: str) -> None:
        logging.error(message)
    
    def critical(self, message: str) -> None:
        logging.critical(message)
