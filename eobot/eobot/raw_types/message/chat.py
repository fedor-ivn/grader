from typing import TypeVar
from eobot.raw_types.raw import RawType
from eobot.tgtypes.message.message import Chat


T = TypeVar("T")


class RawChat(RawType[Chat]):
    def parse(self) -> Chat:
        return Chat(id=self._raw.get("id"))  # type: ignore
