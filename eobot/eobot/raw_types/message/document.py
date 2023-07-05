from __future__ import annotations
from dataclasses import fields
from eobot.raw_types.raw import RawType
from eobot.tgtypes.document import Document


class RawDocument(RawType[Document]):
    def parse(self) -> Document:
        self._log.debug("Parsing raw document")
        self._log.debug(str(self._raw))
        required_args = {
            key: self._raw.get(key)
            for key in map(
                lambda field: field.name, fields(Document)
            )
        }
        return Document(**required_args)  # type: ignore
