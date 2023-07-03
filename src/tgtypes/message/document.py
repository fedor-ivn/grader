from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from tgtypes.message.message import Message
from tgtypes.message.text import AbstractText, NoText
from update.message.document import DocumentMessageUpdate

if TYPE_CHECKING:
    from tgtypes.document import Document


@dataclass
class DocumentMessage(
    Message[DocumentMessageUpdate],
):
    document: Document
    caption: AbstractText = NoText()

    def construct_update(
        self, update_id: int
    ) -> DocumentMessageUpdate:
        return DocumentMessageUpdate(update_id, self)
