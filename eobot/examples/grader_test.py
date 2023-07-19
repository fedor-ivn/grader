import logging
import os
import pprint
from typing import Any

from arguments.message.replying import ReplyingMessage
from bot.inner_bot import Bot
from bot.token import DotenvToken
from arguments.keyboard.button import Button
from arguments.keyboard.keyboard import ReplyKeyboard
from eobot.arguments.keyboard.abstract import (
    AbstractKeyboard,
)
from eobot.arguments.keyboard.grid import GridKeyboard
from bot.inner_bot import Bot
from eobot.update.filter.text import OnMatchedText
from tgtypes.message.text import TextMessage
from eobot.update.message.text import OnTextMessage
from event_loop import EventLoop
from eobot.arguments.message.text import (
    MarkdownV2Text,
    MessageText,
    PlainText,
)
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from methods.send_message import SendMessage
from update.events import Events
from tgtypes.message.document import (
    DocumentMessage,
)
from polling import Polling, PollingConfig
from dotenv.main import DotEnv

from logger.log import LogConfig
from eobot.update.message.document import OnDocumentMessage
from update.message.unknown import (
    UnknownMessageWarning,
)
from grader.ibash.ibash import IBash

from grader.source_directory.directory import (
    SourceDirectory,
)
from grader.source_directory.files_healthcheck import (
    TaskFilesHealthcheck,
)
from grader.source_directory.required_file import (
    TaskFileGitkeep,
)
from grader.task.directory import TasksDirectory
from grader.task.symlink import TasksSymlinks

from grader.task.active_tasks import ActiveTasks

from grader.tests.test import Test


class GreetingText(MessageText):
    def to_dict(self) -> dict[str, Any]:
        return PlainText(
            """
Hello and welcome to the Task Grading Bot!

I am here to assist you with grading the tasks. With my
help, you can evaluate your progress on the task, receive
your score and feedback.

To get started, send /grade command to me.

In case of any problems, do not hesitate to contact the
developers:

- @fedor_ivn
- @Probirochniy
"""
        ).to_dict()


class FSM:
    def __init__(self, states: list[str]) -> None:
        self._states = states

    def initial(self) -> str:
        return self._states[0]

    def next(self, state: str) -> str:
        return self._states[
            (self._states.index(state) + 1)
            % len(self._states)
        ]


class UserState:
    def __init__(
        self, user_id: int, fsm: FSM, database
    ) -> None:
        self._user_id = user_id
        self._fsm = fsm
        self._database = database

    def next(self) -> "UserState":
        return UserState(
            self._user_id, self._fsm, self._database
        )


class TasksKeyboard(AbstractKeyboard):
    def __init__(self, tasks_directory: TasksDirectory):
        self._tasks_directory = tasks_directory

    def to_dict(self) -> dict[str, Any]:
        return GridKeyboard(
            [
                Button(task.name())
                for task in self._tasks_directory.tasks()
            ],
            2,
        ).to_dict()


class Hello(OnTextMessage):
    def __init__(
        self,
        tasks_keyboard: TasksKeyboard,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._tasks_keyboard = tasks_keyboard
        self._log = log

    def handle(
        self, bot: Bot, message: TextMessage
    ) -> None:
        bot.call_method(
            SendMessage(
                message.chat.create_destination(),
                GreetingText(),
                reply_markup=self._tasks_keyboard,
                log=self._log,
            )
        )


class GradeTask(OnDocumentMessage):
    def __init__(
        self,
        tasks_directory: TasksDirectory,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._log = log
        self.tasks_directory = tasks_directory

    def handle(
        self, bot: Bot, message: DocumentMessage
    ) -> None:
        fetched_document = bot.call_method(
            message.document.fetch()
        )

        with bot.open_document(fetched_document) as file:
            solution = file.read().decode("utf-8")

            print(solution)

            print(self.tasks_directory.tasks())

            try:
                bot.call_method(
                    SendMessage(
                        message.chat.create_destination(),
                        PlainText(
                            Test(
                                self.tasks_directory.get_task(
                                    "meme-factory"
                                ).criteria()
                            ).output(IBash(solution))
                        ),
                        reply=ReplyingMessage(message.id),
                    )
                )
            except KeyError:
                bot.call_method(
                    SendMessage(
                        message.chat.create_destination(),
                        PlainText(
                            (
                                "Sorry, this task is not implemented "
                                "yet or does not exist."
                            )
                        ),
                    )
                )
            except Exception as e:
                self._log.error(str(e))


if __name__ == "__main__":
    log = LogConfig(
        level=logging.DEBUG,
        format="%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    ).configure()

    script_path = os.path.abspath(os.path.dirname(__file__))
    tasks_directory = TasksDirectory(
        TasksSymlinks(
            f"{script_path}/tasks_directory",
            SourceDirectory(
                f"{script_path}/../../checkers",
                TaskFilesHealthcheck(
                    [
                        # temporary plug to avoid healthcheck errors
                        TaskFileGitkeep(),
                    ]
                ),
                depth=2,
            ),
        ),
    )

    Bot(DotenvToken("BOT_TOKEN", DotEnv(".env"))).start(
        Polling(
            EventLoop(
                Events(
                    on_text_message=[
                        Hello(
                            TasksKeyboard(tasks_directory),
                            log=log,
                        ),
                        OnMatchedText(
                            "/grade",
                            Hello(
                                TasksKeyboard(
                                    tasks_directory
                                ),
                                log=log,
                            ),
                        ),
                    ],
                    on_document_message=[
                        GradeTask(tasks_directory, log=log),
                    ],
                    on_unknown_message=[
                        UnknownMessageWarning(log=log),
                    ],
                    log=log,
                ),
                log=log,
            ),
            PollingConfig(log=log),
            log=log,
        ),
    )
