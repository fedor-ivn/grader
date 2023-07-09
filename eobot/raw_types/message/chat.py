from typing import TypeVar
from raw_types.raw import RawType
from tgtypes.message.message import Chat


T = TypeVar("T")


class RawChat(RawType[Chat]):
    def parse(self) -> Chat:
        return Chat(id=self._raw.get("id"))  # type: ignore
