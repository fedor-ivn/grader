from eobot.methods.method import Method
from content import EmptyRequestContent
from uri.method_uri import MethodURI
from tgtypes.user.me import Me
from eobot.bot.bot import Bot
from methods.raw_method import RawMethod
from uri.uri import URI
from tgtypes.bool_response import BoolResponse
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class LogOut(Method[bool]):
    def call(
        self, bot: URI, log: AbstractLog = NoLog()
    ) -> bool:
        log.debug("LogOut.call")
        return RawMethod(  # type: ignore
            EmptyRequestContent(),
        ).call(MethodURI("logout", bot))
