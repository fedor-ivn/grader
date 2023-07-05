from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from eobot.tgtypes.message.message import Message
from eobot.tgtypes.message.text import AbstractText, NoText
from eobot.update.message.document import DocumentMessageUpdate

if TYPE_CHECKING:
    from eobot.tgtypes.document import Document


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
