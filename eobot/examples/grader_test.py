import logging
import os
from typing import Any
from vedis import Vedis

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
from eobot.arguments.keyboard.reply_keyboard_remove import (
    ReplyKeyboardRemove,
)
from eobot.bot.inner_bot import Bot
from eobot.fsm.fsm import FSM
from eobot.fsm.user_state.abstract import T
from eobot.fsm.user_state.state import UserStates
from eobot.tgtypes.message.text import TextMessage
from eobot.update.filter.state import OnState
from eobot.update.filter.text import OnMatchedText
from eobot.update.message.text import OnTextMessage
from event_loop import EventLoop
from eobot.arguments.message.text import (
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
    TaskFileTestPy,
)
from grader.task.directory import TasksDirectory
from grader.task.symlink import TasksSymlinks


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
        user_states: UserStates[T],
        log: AbstractLog = NoLog(),
    ) -> None:
        self._tasks_keyboard = tasks_keyboard
        self._user_states = user_states
        self._log = log

    def handle(
        self, bot: Bot, message: TextMessage
    ) -> bool:
        bot.call_method(
            SendMessage(
                message.chat.create_destination(),
                GreetingText(),
                reply_markup=self._tasks_keyboard,
                log=self._log,
            )
        )

        self._user_states.next(message.chat.id)
        return True


class ChooseTask(OnTextMessage):
    def __init__(
        self,
        tasks_directory: TasksDirectory,
        user_states: UserStates[T],
        db: Vedis,
        log: AbstractLog = NoLog(),
    ) -> None:
        self.tasks_directory = tasks_directory
        self._user_states = user_states
        self._log = log
        self._db = db

    def handle(
        self, bot: Bot, message: TextMessage
    ) -> bool:
        if not self.tasks_directory.is_present(
            message.text.value
        ):
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
            return True

        self._db[message.chat.id] = message.text.value
        bot.call_method(
            SendMessage(
                message.chat.create_destination(),
                PlainText("Now send me your solution!"),
                reply=ReplyingMessage(message.id),
                reply_markup=ReplyKeyboardRemove(),
                log=self._log,
            )
        )

        self._user_states.next(message.chat.id)
        return True


class GradeTask(OnDocumentMessage):
    def __init__(
        self,
        tasks_directory: TasksDirectory,
        user_states: UserStates[T],
        db_tasks: Vedis,
        log: AbstractLog = NoLog(),
    ) -> None:
        self.tasks_directory = tasks_directory
        self._user_states = user_states
        self._db_tasks = db_tasks
        self._log = log

    def handle(
        self, bot: Bot, message: DocumentMessage
    ) -> bool:
        fetched_document = bot.call_method(
            message.document.fetch()
        )

        with bot.open_document(fetched_document) as file:
            solution = file.read().decode("utf-8")

            self._log.debug(solution)

            self._log.debug(
                str(self.tasks_directory.tasks())
            )

            try:
                bot.call_method(
                    SendMessage(
                        message.chat.create_destination(),
                        PlainText(
                            self.tasks_directory.task(
                                self._db_tasks[
                                    message.chat.id
                                ].decode("utf-8")
                            ).output(IBash(solution))
                        ),
                        reply=ReplyingMessage(message.id),
                    )
                )
            except Exception as e:
                self._log.error(str(e))
        self._user_states.next(message.chat.id)
        return True


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
                        TaskFileTestPy(),
                    ]
                ),
                depth=2,
            ),
        ),
    )

    start: OnState[OnTextMessage] = OnState(
        "start", log=log
    )
    choose_task: OnState[OnTextMessage] = OnState(
        "choose_task", log=log
    )
    grade_task: OnState[OnDocumentMessage] = OnState(
        "grade_task", log=log
    )

    db_tasks = Vedis(":mem:")
    user_states: UserStates[
        OnTextMessage | OnDocumentMessage
    ] = UserStates(
        FSM([start, choose_task, grade_task]),
        Vedis(":mem:"),
    )

    Bot(DotenvToken("BOT_TOKEN", DotEnv(".env"))).start(
        Polling(
            EventLoop(
                Events(
                    on_text_message=[
                        start.with_states(user_states).do(
                            Hello(  # type: ignore
                                TasksKeyboard(
                                    tasks_directory
                                ),
                                user_states,
                                log=log,
                            )
                        ),
                        choose_task.with_states(
                            user_states
                        ).do(
                            ChooseTask(  # type: ignore
                                tasks_directory,
                                user_states,
                                db_tasks,
                            ),
                        ),
                    ],
                    on_document_message=[
                        grade_task.with_states(
                            user_states
                        ).do(
                            GradeTask(  # type: ignore
                                tasks_directory,
                                user_states,
                                db_tasks,
                                log=log,
                            )
                        )
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
