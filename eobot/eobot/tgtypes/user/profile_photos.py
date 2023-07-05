from dataclasses import dataclass
from tgtypes.photo_size import PhotoSize


@dataclass
class ProfilePhotos:
    total_count: int
    photos: list[list[PhotoSize]]
