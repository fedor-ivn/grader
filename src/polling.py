from time import sleep
from arguments.argument import MethodArgument
from arguments.empty import EmptyArgument
from arguments.inline import InlineArgument
from arguments.merged import MergedArgument
from bot.inner_bot import Bot
from event_loop import EventLoop
from arguments.get_updates.get_updates import (
    GetUpdatesArguments,
)
from methods.get_updates import GetUpdates


class Polling:
    def __init__(
        self,
        bot: Bot,
        event_loop: EventLoop,
        arguments: GetUpdatesArguments = GetUpdatesArguments(),
        poll_interval_ms: int = 25,
    ) -> None:
        self._bot = bot
        self._event_loop = event_loop
        self._arguments = arguments
        self._poll_interval = poll_interval_ms
        self.updated_offset: MethodArgument = (
            EmptyArgument()
        )

    def start(self) -> None:
        while True:
            try:
                updates = self._bot.call_method(
                    GetUpdates(
                        MergedArgument(
                            self._arguments,
                            self.updated_offset,
                        )
                    )
                )
                self._event_loop.handle_updates(
                    self._bot, updates
                )
                self.updated_offset = (
                    updates.updated_offset()
                )
                sleep(self._poll_interval / 1000)
            except KeyboardInterrupt:
                break
