from dataclasses import dataclass
from tg_types.photo_size import PhotoSize


@dataclass
class ProfilePhotos:
    total_count: int
    photos: list[list[PhotoSize]]
