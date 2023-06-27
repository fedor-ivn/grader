from dataclasses import fields
from raw_types.raw import RawType
from tgtypes.message.message_entity import (
    MessageEntity,
    Mention,
    Hashtag,
    Cashtag,
    BotCommand,
    Url,
    Email,
    PhoneNumber,
    Bold,
    Italic,
    Underline,
    Spoiler,
    Strikethrough,
    Code,
    Pre,
    TextLink,
    TextMention,
    CustomEmoji,
)
from exceptions import UnexpectedResponseException


class RawEntity(RawType[MessageEntity]):
    def parse(self) -> MessageEntity:
        required_args = {
            key: self._raw.get(key)
            for key in map(
                lambda field: field.name,
                fields(MessageEntity),
            )
        }
        # https://core.telegram.org/bots/api#messageentity
        match self._raw:
            case {"type": "mention"}:
                return Mention(**required_args)  # type: ignore

            case {"type": "hashtag"}:
                return Hashtag(**required_args)  # type: ignore

            case {"type": "cashtag"}:
                return Cashtag(**required_args)  # type: ignore

            case {"type": "bot_command"}:
                return BotCommand(**required_args)  # type: ignore

            case {"type": "url"}:
                return Url(**required_args)  # type: ignore

            case {"type": "email"}:
                return Email(**required_args)  # type: ignore

            case {"type": "phone_number"}:
                return PhoneNumber(**required_args)  # type: ignore

            case {"type": "bold"}:
                return Bold(**required_args)  # type: ignore

            case {"type": "italic"}:
                return Italic(**required_args)  # type: ignore

            case {"type": "underline"}:
                return Underline(**required_args)  # type: ignore

            case {"type": "spoiler"}:
                return Spoiler(**required_args)  # type: ignore

            case {"type": "strikethrough"}:
                return Strikethrough(**required_args)  # type: ignore

            case {"type": "code"}:
                return Code(**required_args)  # type: ignore

            case {"type": "pre", "language": language}:
                return Pre(**required_args, language=language)  # type: ignore

            case {"type": "text_link", "url": url}:
                return TextLink(**required_args, url=url)  # type: ignore

            case {"type": "text_mention", "user": user}:
                return TextMention(**required_args, user=user)  # type: ignore

            case {
                "type": "custom_emoji",
                "custom_emoji_id": custom_emoji_id,
            }:
                return CustomEmoji(**required_args, custom_emoji_id=custom_emoji_id)  # type: ignore

            case _:
                raise UnexpectedResponseException
