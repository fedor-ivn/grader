from typing import Any
from tgtypes.message.message import Message
from update.update import MessageUpdate

from update.updates import Updates


class RawUpdates:
    def __init__(
        self, raw_updates: list[dict[str, Any]]
    ) -> None:
        self._raw_updates = raw_updates

    def parse(self) -> Updates:
        updates = []
        for raw_update in self._raw_updates:
            update_id = raw_update.pop("update_id")
            match raw_update:
                case {"message": raw_message}:
                    updates.append(
                        MessageUpdate(
                            update_id,
                            Message(**raw_message),
                        )
                    )
                case _:
                    raise NotImplementedError(
                        "This type of update is not implemented yet."
                    )
        return Updates(updates)
