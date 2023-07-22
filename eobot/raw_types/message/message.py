from typing import TypeVar
from raw_types.message.chat import RawChat
from raw_types.message.document import RawDocument
from raw_types.message.raw_entity import RawEntity
from raw_types.raw import RawType
from tgtypes.message.document import DocumentMessage

from tgtypes.message.message import Message

from tgtypes.message.text import Text, TextMessage
from tgtypes.message.unknown import UnknownMessage

T = TypeVar("T")


class RawMessage(RawType[Message[T]]):
    def parse(self) -> Message[T]:
        self._log.debug("Parsing raw message")
        required_args = {
            "id": self._raw.get("message_id"),
            "chat": RawChat(self._raw.get("chat")).parse(),  # type: ignore
            "date": self._raw.get("date"),
        }

        self._log.debug(f"Raw data: {self._raw}")
        match self._raw:
            case {
                "document": document,
                "caption": str(caption),
                "caption_entities": list(raw_entities),
            }:
                return DocumentMessage(
                    document=RawDocument(
                        document, self._log
                    ).parse(),
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
                    document=RawDocument(
                        document, self._log
                    ).parse(),
                    caption=Text(caption),
                    **required_args,  # type: ignore
                )
            case {
                "document": document,
            }:
                return DocumentMessage(
                    document=RawDocument(
                        document, self._log
                    ).parse(),
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
                return UnknownMessage(
                    raw=self._raw, **required_args  # type: ignore
                )
