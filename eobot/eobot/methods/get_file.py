from __future__ import annotations
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from eobot.arguments.inline import InlineArgument
from eobot.content import JsonRequestContent
from eobot.methods.raw_method import RawMethod
from eobot.methods.method import Method
from eobot.raw_types.message.fetched_document import (
    RawFetchedDocument,
)
from eobot.uri.method_uri import MethodURI
from eobot.uri.uri import URI
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eobot.tgtypes.fetched_document import FetchedDocument


class GetFile(Method["FetchedDocument"]):
    def __init__(self, file_id: str) -> None:
        self.file_id = file_id

    def call(
        self, bot: URI, log: AbstractLog = NoLog()
    ) -> "FetchedDocument":
        log.debug("GetFile call")
        return RawFetchedDocument(
            RawMethod(
                JsonRequestContent(
                    InlineArgument(
                        "file_id", self.file_id
                    ).to_dict()
                ),
            ).call(MethodURI("getFile", bot))
        ).parse()
