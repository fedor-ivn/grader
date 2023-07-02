from dataclasses import dataclass
from typing import Any
from tgtypes.message.message import Message
from update.message.unknown import UnknownMessageUpdate


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
