from source_directory.directory import SourceDirectory
from source_directory.files_healthcheck import (
    TaskFilesHealthcheck,
)
from source_directory.required_file import TaskFileGitkeep
from task.directory import TasksDirectory
from task.symlink import TasksSymlinks


tasks = TasksDirectory(
    TasksSymlinks(
        "tasks-dictionary",
        SourceDirectory(
            "checkers",
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

print(tasks.get_task("review-book").task_path)
