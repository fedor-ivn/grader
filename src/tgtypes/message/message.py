from abc import ABC
from dataclasses import dataclass, field
from typing import TypeVar
from arguments.message.destination import Destination

from tgtypes.message.message_entity import MessageEntity
from update.construct_update import UpdateFactory
from update.message.document import DocumentMessageUpdate

from update.message.text import TextMessageUpdate


@dataclass
class Chat:
    id: int

    def create_destination(self) -> Destination:
        return Destination(chat_id=self.id)


T = TypeVar("T")


@dataclass
class Message(UpdateFactory[T]):
    id: int
    date: int
    chat: Chat


class AbstractText:
    pass


@dataclass
class Text(AbstractText):
    value: str
    entities: list[MessageEntity] = field(
        default_factory=list
    )


class NoText(AbstractText):
    def __init__(self) -> None:
        self.value = ""
        self.entities: list[MessageEntity] = []


@dataclass
class TextMessage(
    Message[TextMessageUpdate],
):
    text: Text

    def construct_update(
        self, update_id: int
    ) -> TextMessageUpdate:
        return TextMessageUpdate(update_id, self)


@dataclass
class Document:
    file_id: str
    file_unique_id: str


@dataclass
class DocumentMessage(
    Message[DocumentMessageUpdate],
):
    document: Document
    caption: AbstractText = NoText()

    def construct_update(
        self, update_id: int
    ) -> DocumentMessageUpdate:
        return DocumentMessageUpdate(update_id, self)

    # media_group_id: str | None = None


# todo: дамир, ну и нахуя ты это написал?
# ты же знаешь, что это говно

# official answer from dameer:
# бля да я ж второпях перенёс чисто всю хуйню шобы разбить потом
# за что хейт

# @dataclass
# class Message:
#     message_id: int
#     message_thread_id: int
#     message_from: User
#     sender_chat: Chat
#     date: int
#     chat: Chat
#     forward_from: User
#     forward_from_chat: Chat
#     forward_from_message_id: int
#     forward_signature: str
#     forward_sender_name: str
#     forward_date: int
#     is_topic_message: bool
#     is_automatic_forward: bool
#     reply_to_message: Message
#     via_bot: User
#     edit_date: int
#     has_protected_content: bool
#     media_group_id: str
#     author_signature: str
#     text: str
#     entities: list[MessageEntry]
#     animation: Animation
#     audio: Audio
#     document: Document
#     photo: list[PhotoSize]
#     sticker: Sticker
#     video: Video
#     video_note: VideoNote
#     voice: Voice
#     caption: str
#     caption_entities: list[MessageEntry]
#     has_media_spoiler: bool
#     contact: Contact
#     dice: Dice
#     game: Game
#     poll: Poll
#     venue: Venue
#     location: Location
#     new_chat_members: list[User]
#     left_chat_member: User
#     new_chat_title: str
#     new_chat_photo: list[PhotoSize]
#     delete_chat_photo: bool
#     group_chat_created: bool
#     supergroup_chat_created: bool
#     channel_chat_created: bool
#     message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged
#     migrate_to_chat_id: int
#     migrate_from_chat_id: int
#     pinned_message: Message
#     invoice: Invoice
#     successful_payment: SuccessfulPayment
#     user_shared: UserShared
#     chat_shared: ChatShared
#     connected_website: String
#     write_access_allowed: WriteAccessAllowed
#     passport_data: PassportData
#     proximity_alert_triggered: ProximityAlertTriggered
#     forum_topic_created: ForumTopicCreated
#     forum_topic_edited: ForumTopicEdited
#     forum_topic_closed: ForumTopicClosed
#     forum_topic_reopened: ForumTopicReopened
#     general_forum_topic_hidden: GeneralForumTopicHidden
#     general_forum_topic_unhidden: GeneralForumTopicUnhidden
#     video_chat_scheduled: VideoChatScheduled
#     video_chat_started: VideoChatStarted
#     video_chat_ended: VideoChatEnded
#     video_chat_participants_invited: VideoChatParticipantsInvited
#     web_app_data: WebAppData
#     reply_markup: InlineKeyboardMarkup
