from dataclasses import dataclass


@dataclass
class MessageEntity:
    type: str
    offset: int
    length: int
    # url: Optional[str] = None
    # user: Optional[User] = None
    # language: Optional[str] = None
