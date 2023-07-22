from urllib.request import urlopen
from bot.inner_bot import Bot
from dataclasses import dataclass
from typing import Any


@dataclass
class FetchedDocument:
    file_id: str
    file_unique_id: str
    file_path: str

    def open(self, bot: Bot) -> Any:
        # print(f"{bot.construct_file_uri()}{self.file_path}")
        return urlopen(
            f"{bot.construct_file_uri()}{self.file_path}"
        )
