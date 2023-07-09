from dataclasses import dataclass

from arguments.message.destination import Destination


@dataclass
class Chat:
    id: int

    def create_destination(self) -> Destination:
        return Destination(chat_id=self.id)
