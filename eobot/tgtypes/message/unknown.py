from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any
from update.message.unknown import (
    UnknownMessageUpdate,
)
from tgtypes.message.message import Message

# if TYPE_CHECKING:


@dataclass
class UnknownMessage(Message[UnknownMessageUpdate]):
    """
    This message type is probably not implemented yet or is not supported
    """

    raw: dict[str, Any]

    def construct_update(
        self, update_id: int
    ) -> UnknownMessageUpdate:
        return UnknownMessageUpdate(update_id, self)
