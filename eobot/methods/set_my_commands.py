from eobot.methods.method import Method
from content import EmptyRequestContent, JsonRequestContent
from uri.method_uri import MethodURI
from methods.raw_method import RawMethod
from uri.uri import URI
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from eobot.arguments.bot.command import BotCommand


class SetMyCommands(Method[bool]):
    def __init__(self, commands: list[BotCommand]) -> None:
        self._commands = commands

    def call(
        self, bot: URI, log: AbstractLog = NoLog()
    ) -> bool:
        log.debug(
            f"Setting {len(self._commands)} commands: {self._commands}"
        )

        return RawMethod(  # type: ignore
            JsonRequestContent(
                {
                    "commands": [
                        command.to_dict()
                        for command in self._commands
                    ],
                }
            ),
        ).call(MethodURI("setMyCommands", bot))
