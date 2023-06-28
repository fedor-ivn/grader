from dataclasses import fields
from typing import Any, TypeVar
from exceptions import UnexpectedResponseException
from raw_types.message.document import RawDocument
from raw_types.message.raw_entity import RawEntity
from raw_types.raw import RawType

from tgtypes.message.message import (
    DocumentMessage,
    Message,
    Text,
    TextMessage,
)

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog

T = TypeVar("T")


class RawMessage(RawType[Message[T]]):
    def parse(self) -> Message[T]:
        self._log.debug("Parsing raw message")
        replaces = {
            "message_id": "id",
        }
        required_args = {
            replaces.get(key, key): self._raw.get(key)
            for key in map(
                lambda field: field.name,
                fields(Message),
            )
        }
        self._log.debug(f"Raw data: {self._raw}")
        match self._raw:
            case {
                "document": document,
                "caption": str(caption),
                "caption_entities": list(raw_entities),
            }:
                return DocumentMessage(
                    document=RawDocument(document).parse(),
                    caption=Text(
                        caption,
                        [
                            RawEntity(raw).parse()
                            for raw in raw_entities
                        ],
                    ),
                    **required_args,  # type: ignore
                )
            case {
                "document": document,
                "caption": str(caption),
            }:
                return DocumentMessage(
                    document=RawDocument(document).parse(),
                    caption=Text(caption),
                    **required_args,  # type: ignore
                )
            case {
                "document": document,
            }:
                return DocumentMessage(
                    document=RawDocument(document).parse(),
                    caption=Text(""),
                    **required_args,  # type: ignore
                )
            case {
                "text": str(text),
                "entities": list(raw_entities),
            }:
                self._log.debug(
                    "Message is text message with entities"
                )
                return TextMessage(
                    text=Text(
                        text,
                        [
                            RawEntity(raw).parse()
                            for raw in raw_entities
                        ],
                    ),
                    **required_args,  # type: ignore
                )
            case {"text": str(text)}:
                self._log.debug(
                    "Message is text message without entities"
                )
                return TextMessage(
                    text=Text(text),
                    **required_args,  # type: ignore
                )
            case _:
                self._log.debug(
                    "This message type is probably not implemented yet or is not supported"
                )
                raise UnexpectedResponseException
