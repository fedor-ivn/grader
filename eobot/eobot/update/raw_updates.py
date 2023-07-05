from typing import Any
from eobot.raw_types.message.message import RawMessage
from eobot.tgtypes.message.message import Message
from eobot.update.update import Update

from eobot.update.updates import Updates

from logger.abstract_log import AbstractLog
from logger.no_log import NoLog


class RawUpdates:
    def __init__(
        self,
        raw_updates: list[dict[str, Any]],
        log: AbstractLog = NoLog(),
    ) -> None:
        self._raw_updates = raw_updates
        self._log = log

    def parse(self) -> Updates:
        self._log.debug("Parsing raw updates...")
        updates: list[Update] = []
        for raw_update in self._raw_updates:
            self._log.debug(
                f"Parsing raw update: {raw_update}"
            )
            update_id = raw_update.pop("update_id")
            match raw_update:
                case {"message": raw_message}:
                    self._log.debug(
                        f"Parsing raw message: {raw_message}"
                    )
                    updates.append(
                        RawMessage(raw_message, self._log)
                        .parse()
                        .construct_update(update_id)
                    )
                case _:
                    self._log.error(
                        f"Unknown update type: {raw_update}"
                    )
                    raise NotImplementedError(
                        "This type of update is not implemented yet."
                    )
        return Updates(updates)
