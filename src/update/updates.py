from typing import Any

# class Handlers:
#     def __init__(self, message_handlers: list[Handler] = [], ) -> None:


# class MessageUpdate(Update):
#     _id: int
#     _message: Message

#     def handle(self, handlers: Handlers):
#         handlers.handle_message(self._message)


class Updates:
    def __init__(self, raw_updates: dict[str, Any]) -> None:
        self._raw_updates = raw_updates
        # self.messages =

    # def parse(self) -> None:

    # messages: list[Message],
    # edited_messages: list[Message],
    # channel_posts: list[Message],
    # edited_channel_posts: list[Message],
    # inline_queries: list[InlineQuery],
