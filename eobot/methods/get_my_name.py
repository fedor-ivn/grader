from eobot.tgtypes.bot.name import BotName
from eobot.methods.method import Method
from content import EmptyRequestContent
from uri.method_uri import MethodURI
from tgtypes.user.me import Me
from methods.raw_method import RawMethod
from uri.uri import URI
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class GetMyName(Method[BotName]):
    def __init__(self, log: AbstractLog = NoLog()) -> None:
        self._log = log

    def call(self, bot: URI) -> BotName:
        return BotName(
            **RawMethod(
                EmptyRequestContent(),
            ).call(MethodURI("getMyName", bot))
        )
