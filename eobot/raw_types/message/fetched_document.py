from __future__ import annotations
from dataclasses import fields
from raw_types.raw import RawType
from tgtypes.fetched_document import FetchedDocument


class RawFetchedDocument(RawType[FetchedDocument]):
    def parse(self) -> FetchedDocument:
        self._log.debug("Parsing raw fetched document")
        self._log.debug(str(self._raw))
        required_args = {
            key: self._raw.get(key)
            for key in map(
                lambda field: field.name,
                fields(FetchedDocument),
            )
        }
        return FetchedDocument(**required_args)  # type: ignore
