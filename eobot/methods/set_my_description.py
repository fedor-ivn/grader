from eobot.methods.method import Method
from content import JsonRequestContent
from uri.method_uri import MethodURI
from methods.raw_method import RawMethod
from uri.uri import URI
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class SetMyDescription(Method[bool]):
    def __init__(
        self, description: str, log: AbstractLog = NoLog()
    ) -> None:
        self._description = description
        self._log = log

    def call(self, bot: URI) -> bool:
        return RawMethod(  # type: ignore
            JsonRequestContent(
                {
                    "description": self._description,
                }
            )
        ).call(MethodURI("setMyDescription", bot))
