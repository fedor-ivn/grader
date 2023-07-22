from eobot.methods.method import Method
from content import JsonRequestContent
from uri.method_uri import MethodURI
from methods.raw_method import RawMethod
from uri.uri import URI
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class SetMyShortDescription(Method[bool]):
    def __init__(
        self,
        short_description: str,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._short_description = short_description
        self._log = log

    def call(self, bot: URI) -> bool:
        return RawMethod(  # type: ignore
            JsonRequestContent(
                {
                    "short_description": self._short_description,
                }
            )
        ).call(MethodURI("setMyShortDescription", bot))
