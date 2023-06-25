import pprint
from arguments.empty import EmptyArgument
from methods.method import Method
from content import JsonRequestContent
from methods.raw_method import RawMethod
from tgtypes.message.message import Message
from update.raw_updates import RawUpdates
from update.update import MessageUpdate, Update
from update.updates import Updates
from uri.method_uri import MethodURI
from uri.uri import URI
from typing import Any
from arguments.argument import (
    MethodArgument,
)


class GetUpdates(Method[Updates]):
    def __init__(
        self,
        arguments: MethodArgument = EmptyArgument(),
    ) -> None:
        self._arguments = arguments

    def call(self, bot: URI) -> Updates:
        return RawUpdates(
            RawMethod(
                JsonRequestContent(
                    self._arguments.to_dict()
                ),
            ).call(MethodURI("getUpdates", bot))
        ).parse()
