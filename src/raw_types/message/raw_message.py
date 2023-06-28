from dataclasses import fields
from typing import Any
from raw_types.message.raw_entity import RawEntity
from raw_types.raw import RawType

from tgtypes.message.message import (
    Message,
    Text,
    TextMessage,
)

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class RawMessage(RawType[Message]):
    def parse(self) -> Message:
        self._log.debug("Parsing raw message")
        required_args = {
            key: self._raw.get(key)
            for key in map(
                lambda field: field.name, fields(Message)
            )
        }
        match self._raw:
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
        return Message(**self._raw)
