from dataclasses import dataclass, field
from eobot.tgtypes.message.message import Message

from eobot.tgtypes.message.message_entity import MessageEntity
from eobot.update.message.text import TextMessageUpdate


class AbstractText:
    pass


@dataclass
class Text(AbstractText):
    value: str
    entities: list[MessageEntity] = field(
        default_factory=list
    )


class NoText(AbstractText):
    def __init__(self) -> None:
        self.value = ""
        self.entities: list[MessageEntity] = []


@dataclass
class TextMessage(
    Message[TextMessageUpdate],
):
    text: Text

    def construct_update(
        self, update_id: int
    ) -> TextMessageUpdate:
        return TextMessageUpdate(update_id, self)
