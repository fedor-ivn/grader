from dataclasses import fields
from raw_types.raw import RawType

from tgtypes.message.message import Document


class RawDocument(RawType[Document]):
    def parse(self) -> Document:
        self._log.debug("Parsing raw document")
        required_args = {
            key: self._raw.get(key)
            for key in map(
                lambda field: field.name, fields(Document)
            )
        }
        return Document(**required_args)  # type: ignore
