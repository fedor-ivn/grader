from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any
from urllib.request import urlopen

from methods.get_file import GetFile

if TYPE_CHECKING:
    from bot.inner_bot import Bot


@dataclass
class Document:
    file_id: str
    file_unique_id: str

    def fetch(self) -> GetFile:
        return GetFile(self.file_id)
