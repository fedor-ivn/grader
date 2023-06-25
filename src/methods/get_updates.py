import pprint
from method_arguments.empty import EmptyArgument
from methods.method import Method
from content import JsonRequestContent
from methods.raw_method import RawMethod
from tgtypes.message.message import Message
from update.update import MessageUpdate, Update
from update.updates import Updates
from uri.method_uri import MethodURI
from uri.uri import URI
from typing import Any
from method_arguments.method_argument import (
    AbstractMethodArgument,
)


class RawUpdates:
    def __init__(
        self, raw_updates: list[dict[str, Any]]
    ) -> None:
        self._raw_updates = raw_updates

    def to_list(self) -> list[Update]:
        updates = []
        pprint.pprint(self._raw_updates)
        for raw_update in self._raw_updates:
            raw_update.pop("update_id")
            match raw_update:
                case {
                    "message": raw_message,
                    "update_id": update_id,
                }:
                    updates.append(
                        MessageUpdate(
                            update_id,
                            Message(**raw_message),
                        )
                    )
                case _:
                    raise NotImplementedError(
                        "This type of update is not implemented yet."
                    )
        return updates  # type: ignore


class GetUpdates(Method[list[Update]]):
    def __init__(
        self,
        arguments: AbstractMethodArgument = EmptyArgument(),
    ) -> None:
        self._arguments = arguments

    def call(self, bot: URI) -> list[Update]:
        return RawUpdates(
            RawMethod(
                JsonRequestContent(
                    self._arguments.to_dict()
                ),
            ).call(MethodURI("getUpdates", bot))
        ).to_list()
