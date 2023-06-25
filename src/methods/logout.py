from methods.method import Method
from content import EmptyRequestContent
from uri.method_uri import MethodURI
from tgtypes.user.me import Me
from bot.inner_bot import Bot
from methods.raw_method import RawMethod
from uri.uri import URI


class LogOut(Method[Me]):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    def call(self, bot: URI) -> Me:
        return Me(
            **RawMethod(
                EmptyRequestContent(),
            ).call(MethodURI("logout", bot))
        )
