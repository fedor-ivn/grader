from dataclasses import dataclass, field
import re
from eobot.tgtypes.message.message import Message

from eobot.tgtypes.message.entity import (
    MessageEntity,
)
from update.message.text import TextMessageUpdate


class AbstractText:
    pass


@dataclass
class Text(AbstractText):
    value: str
    entities: list[MessageEntity] = field(
        default_factory=list
    )

    def match(self, regex: str) -> bool:
        result = re.search(regex, self.value)
        if result:
            return True
        else:
            return False


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
