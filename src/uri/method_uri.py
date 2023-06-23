from bot.inner_bot import Bot
from uri.uri import URI


class MethodURI(URI):
    def __init__(self, method: str, bot: Bot) -> None:
        self._method = method
        self._bot = bot

    def construct_uri(self) -> str:
        return f"{self._bot.construct_uri()}{self._method}"
