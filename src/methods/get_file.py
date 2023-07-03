from __future__ import annotations
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from arguments.inline import InlineArgument
from content import JsonRequestContent
from methods.raw_method import RawMethod
from raw_types.message.document import RawDocument
from methods.method import Method
from uri.method_uri import MethodURI
from uri.uri import URI
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tgtypes.message.message import Document


class GetFile(Method[Document]):
    def __init__(self, file_id: str) -> None:
        self.file_id = file_id

    def call(
        self, bot: URI, log: AbstractLog = NoLog()
    ) -> Document:
        log.debug("GetFile call")
        return RawDocument(
            RawMethod(
                JsonRequestContent(
                    InlineArgument(
                        "file_id", self.file_id
                    ).to_dict()
                ),
            ).call(MethodURI("getFile", bot))
        ).parse()
