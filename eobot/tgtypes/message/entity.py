from dataclasses import dataclass

from tgtypes.user.user import User


@dataclass
class MessageEntity:
    offset: int
    length: int


class Mention(MessageEntity):
    pass


class Hashtag(MessageEntity):
    pass


class Cashtag(MessageEntity):
    pass


class BotCommand(MessageEntity):
    pass


class Url(MessageEntity):
    pass


class Email(MessageEntity):
    pass


class PhoneNumber(MessageEntity):
    pass


class Bold(MessageEntity):
    pass


class Italic(MessageEntity):
    pass


class Underline(MessageEntity):
    pass


class Spoiler(MessageEntity):
    pass


class Strikethrough(MessageEntity):
    pass


class Code(MessageEntity):
    pass


class Pre(MessageEntity):
    language: str


class TextLink(MessageEntity):
    url: str


class TextMention(MessageEntity):
    user: User


class CustomEmoji(MessageEntity):
    custom_emoji_id: int
