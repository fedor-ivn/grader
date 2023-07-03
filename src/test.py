import logging
from typing import Any

from arguments.message.replying import ReplyingMessage
from bot.inner_bot import Bot
from bot.token import DotenvToken
from event_loop import EventLoop
from arguments.message.text import PlainText
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
from update.message.document import OnDocumentMessage
from update.message.unknown import UnknownMessageWarning
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

            task = tasks.get_task("meme-factory")
            print(task.task_path)
            with open(
                f"{task.task_path}/test.py"
            ) as grader:
                print(grader.read())

            with open("solution.sh", "w") as solution_file:
                solution_file.write(solution)

            Test().output(IBash("solution.sh"))  # type: ignore

            bot.call_method(
                SendMessage(
                    message.chat.create_destination(),
                    PlainText("Иди в пизду!"),
                    reply=ReplyingMessage(message.id),
                )
            )


if __name__ == "__main__":
    # todo: call source directory
    tasks_directory = tasks = TasksDirectory(
        TasksSymlinks(
            "tasks_directory",
            SourceDirectory(
                "../checkers",
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
    task = tasks.get_task("meme-factory")
    print(task.task_path)
    with open(f"{task.task_path}/test.py") as grader:
        grader_code = grader.read()
    # todo: import grader on a fly
    # https://stackoverflow.com/questions/301134/how-can-i-import-a-module-dynamically-given-its-name-as-string

    Test().output(IBash("solution.sh"))  # type: ignore

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

# GetMe(bot).call()
# print(GetUserProfilePhotos(bot, user_id=742596099).call())

# print(
#     bot.call_method(
#         SendMessage(
#             chat_id=742596099,
#             text=PlainText("Hello!"),
#         )
#     )
# )

# print(
#     bot.call_method(
#         GetUpdates(
#             # chat_id=742596099,
#             # text=PlainText("Hello!"),
#         )
#     )
# )
