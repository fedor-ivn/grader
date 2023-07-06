import logging
from typing import Any

from eobot.arguments.message.replying import ReplyingMessage
from eobot.bot.inner_bot import Bot
from eobot.bot.token import DotenvToken
from eobot.event_loop import EventLoop
from eobot.arguments.message.text import PlainText
from logger.abstract_log import AbstractLog
from logger.no_log import NoLog
from eobot.methods.send_message import SendMessage
from eobot.update.events import Events
from eobot.tgtypes.message.document import (
    DocumentMessage,
)
from eobot.polling import Polling, PollingConfig
from dotenv.main import DotEnv

from logger.log import LogConfig
from eobot.update.message.document import OnDocumentMessage
from eobot.update.message.unknown import UnknownMessageWarning
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

from eobot.examples.task_grader import TaskGrader

import importlib
import importlib.util
import os


class GradeTask(OnDocumentMessage):
    def __init__(
        self,
        source_directory: SourceDirectory,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._log = log
        self.source_directory = source_directory

    def handle(
        self, bot: Bot, message: DocumentMessage
    ) -> None:
        fetched_document = bot.call_method(
            message.document.fetch()
        )

        with bot.open_document(fetched_document) as file:
            solution = file.read().decode("utf-8")

            task_test = TaskGrader(self.source_directory).grader_object("meme-factory")

            print(task_test)

            bot.call_method(
                SendMessage(
                    message.chat.create_destination(),
                    PlainText(task_test().output(IBash("solution.sh"))),
                    reply=ReplyingMessage(message.id),
                )
            )


if __name__ == "__main__":
    # todo: call source directory
    tasks_directory = TasksDirectory(
        TasksSymlinks(
            "tasks_directory",
            SourceDirectory(
                "../../../checkers",
                2,
                TaskFilesHealthcheck(
                    [
                        # temporary plug to avoid healthcheck errors
                        TaskFileGitkeep(),
                        # TaskFileTestPy(),
                        # TaskFileReferenceSolutionSh(),
                        # TaskFileStatementMd(),
                    ]
                ),
            ),
        ),
    )

    log = LogConfig(
        level=logging.ERROR,
        format="%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    ).configure()

    Bot(DotenvToken("BOT_TOKEN", DotEnv(".env"))).start(
        Polling(
            EventLoop(
                Events(
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
