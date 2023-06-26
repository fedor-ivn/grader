from abc import ABC, abstractmethod
from state import State
from time import sleep
from arguments.argument import MethodArgument
from arguments.inline import InlineArgument
from arguments.merged import MergedArgument
from bot.inner_bot import Bot
from event_loop import EventLoop
from arguments.get_updates.get_updates import (
    GetUpdatesArguments,
)
from methods.get_updates import GetUpdates


class Polling(State):
    def __init__(
        self,
        event_loop: EventLoop,
        arguments: GetUpdatesArguments = GetUpdatesArguments(),
        poll_interval_ms: int = 25,
    ) -> None:
        self._event_loop = event_loop
        self._arguments = arguments
        self._poll_interval = poll_interval_ms

    def start(self, bot: Bot) -> None:
        current_offset = 0

        while True:
            try:
                updates = bot.call_method(
                    GetUpdates(
                        self._arguments.with_offset(
                            current_offset
                        )
                    )
                )
                self._event_loop.handle_updates(
                    bot, updates
                )
                current_offset = updates.update_offset(
                    current_offset
                )
                # is it okay to divide by 1000 inplace?
                sleep(self._poll_interval / 1000)
            except KeyboardInterrupt:
                break
