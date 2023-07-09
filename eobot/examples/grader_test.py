import logging
import os
import pprint

from arguments.message.replying import ReplyingMessage
from bot.inner_bot import Bot
from bot.token import DotenvToken
from arguments.keyboard.button import Button
from arguments.keyboard.keyboard import ReplyKeyboard
from bot.inner_bot import Bot
from tgtypes.message.text import TextMessage
from update.message.text import OnTextMessage
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


class SendKeyboard(OnTextMessage):
    def __init__(
        self,
        log: AbstractLog = NoLog(),
    ) -> None:
        self._log = log

    def handle(
        self, bot: Bot, message: TextMessage
    ) -> None:
        bot.call_method(
            SendMessage(
                message.chat.create_destination(),
                PlainText("Hello, world!"),
                reply_markup=ReplyKeyboard([[Button("1")]]),
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
            # todo: Damir переделай это.... что за хрень, почему мы сохраняем
            # солюшн на диск?
            with open("solution.sh", "w") as f:
                f.write(solution)

            try:
                bot.call_method(
                    SendMessage(
                        message.chat.create_destination(),
                        PlainText(
                            self.tasks_directory.get_task(
                                "meme-factory"
                            )
                            .create_test()
                            .output(IBash("solution.sh"))
                        ),
                        reply=ReplyingMessage(message.id),
                    )
                )
            except:
                pass


if __name__ == "__main__":
    log = LogConfig(
        level=logging.DEBUG,
        format="%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    ).configure()
    script_path = os.path.abspath(os.path.dirname(__file__))

    Bot(DotenvToken("BOT_TOKEN", DotEnv(".env"))).start(
        Polling(
            EventLoop(
                Events(
                    on_document_message=[
                        GradeTask(
                            TasksDirectory(
                                TasksSymlinks(
                                    f"{script_path}/tasks_directory",
                                    SourceDirectory(
                                        f"{script_path}../../../checkers",
                                        TaskFilesHealthcheck(
                                            [
                                                # temporary plug to avoid healthcheck errors
                                                TaskFileGitkeep(),
                                            ]
                                        ),
                                        depth=2,
                                    ),
                                ),
                            ),
                            log=log,
                        ),
                    ],
                    on_text_message=[
                        SendKeyboard(log=log),
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
