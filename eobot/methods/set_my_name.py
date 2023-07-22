from eobot.methods.method import Method
from content import JsonRequestContent
from uri.method_uri import MethodURI
from methods.raw_method import RawMethod
from uri.uri import URI
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class SetMyName(Method[bool]):
    def __init__(
        self, name: str, log: AbstractLog = NoLog()
    ) -> None:
        self._name = name
        self._log = log

    def call(self, bot: URI) -> bool:
        return RawMethod(  # type: ignore
            JsonRequestContent(
                {
                    "name": self._name,
                }
            )
        ).call(MethodURI("logout", bot))
