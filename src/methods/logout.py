from methods.method import Method
from content import EmptyContent
from uri.method_uri import MethodURI
from tg_types.user.me import Me
from bot.inner_bot import Bot
from methods.raw_method import RawMethod


class LogOut(Method[Me]):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    def call(self) -> Me:
        return Me(
            **RawMethod(
                MethodURI("logout", self._bot),
                EmptyContent(),
            ).call()
        )
