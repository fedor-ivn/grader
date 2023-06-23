from dataclasses import dataclass
from typing import NewType

FileId = NewType("FileId", str)


@dataclass
class PhotoSize:
    file_id: FileId
    file_unique_id: str
    width: int
    height: int
    file_size: int | None = None
