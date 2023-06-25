from time import sleep
from bot.inner_bot import Bot
from event_loop import EventLoop
from method_arguments.get_updates.get_updates import (
    GetUpdatesArguments,
)
from methods.get_updates import GetUpdates


class Polling:
    def __init__(
        self,
        bot: Bot,
        event_loop: EventLoop,
        arguments: GetUpdatesArguments = GetUpdatesArguments(),
        poll_interval: int = 25,
    ) -> None:
        self._bot = bot
        self._event_loop = event_loop
        self._arguments = arguments
        self._poll_interval = poll_interval

    def run(self) -> None:
        while True:
            try:
                self._event_loop.handle_updates(
                    self._bot,
                    self._bot.call_method(
                        GetUpdates(
                            arguments=self._arguments,
                        )
                    ),
                )
                sleep(self._poll_interval)
            except KeyboardInterrupt:
                break
