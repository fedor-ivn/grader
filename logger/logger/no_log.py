from logger.abstract_log import AbstractLog

class Log(AbstractLog):
    def __init__(self) -> None:
        pass 

    def debug(self, message: str) -> None:
        pass

    def info(self, message: str) -> None:
        pass

    def warning(self, message: str) -> None:
        pass

    def error(self, message: str) -> None:
        pass
    
    def critical(self, message: str) -> None:
        pass