from methods.method import Method
from content import EmptyRequestContent
from uri.method_uri import MethodURI
from tgtypes.user.me import Me
from bot.inner_bot import Bot
from methods.raw_method import RawMethod
from uri.uri import URI
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class GetMe(Method[Me]):
    def call(
        self, bot: URI, log: AbstractLog = NoLog()
    ) -> Me:
        log.debug("GetMe.call")
        return Me(
            **RawMethod(
                EmptyRequestContent(),
            ).call(MethodURI("getMe", bot))
        )
