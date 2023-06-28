import pprint
from arguments.get_updates.allowed_updates import (
    AbstractAllowedUpdates,
    DefaultAllowedUpdates,
)
from arguments.get_updates.get_updates import (
    GetUpdatesArguments,
)
from arguments.inline import InlineArgument
from arguments.method_arguments import MethodArguments
from methods.method import Method
from content import JsonRequestContent
from methods.raw_method import RawMethod
from tgtypes.message.message import Message
from update.raw_updates import RawUpdates
from update.update import Update
from update.updates import Updates
from uri.method_uri import MethodURI
from uri.uri import URI
from typing import Any
from arguments.argument import (
    MethodArgument,
)
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class GetUpdates(Method[Updates]):
    def __init__(
        self,
        offset: int = -1,
        limit: int = 100,
        timeout: int = 0,
        allowed_updates: AbstractAllowedUpdates = DefaultAllowedUpdates(),
        log: AbstractLog = NoLog(),
    ) -> None:
        self._offset = offset
        self._limit = limit
        self._timeout = timeout
        self._allowed_updates = allowed_updates
        self._log = log

    def call(self, bot: URI) -> Updates:
        self._log.debug("GetUpdates.call")
        return RawUpdates(
            RawMethod(
                JsonRequestContent(
                    MethodArguments(
                        [
                            InlineArgument(
                                "offset", self._offset
                            ),
                            InlineArgument(
                                "limit", self._limit
                            ),
                            InlineArgument(
                                "timeout", self._timeout
                            ),
                            self._allowed_updates,
                        ]
                    ).to_dict()
                ),
            ).call(MethodURI("getUpdates", bot))
        ).parse()
