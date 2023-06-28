from typing import Any
from raw_types.message.raw_message import RawMessage
from tgtypes.message.message import Message
from update.update import MessageUpdate

from update.updates import Updates

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class RawUpdates:
    def __init__(
        self,
        raw_updates: list[dict[str, Any]],
        log: AbstractLog = NoLog(),
    ) -> None:
        self._raw_updates = raw_updates
        self.log = log

    def parse(self) -> Updates:
        self.log.debug("Parsing raw updates...")
        updates = []
        for raw_update in self._raw_updates:
            self.log.debug(
                f"Parsing raw update: {raw_update}"
            )
            update_id = raw_update.pop("update_id")
            match raw_update:
                case {"message": raw_message}:
                    self.log.debug(
                        f"Parsing raw message: {raw_message}"
                    )
                    updates.append(
                        MessageUpdate(
                            update_id,
                            RawMessage(raw_message).parse(),
                        )
                    )
                case _:
                    self.log.error(
                        f"Unknown update type: {raw_update}"
                    )
                    raise NotImplementedError(
                        "This type of update is not implemented yet."
                    )
        return Updates(updates)
