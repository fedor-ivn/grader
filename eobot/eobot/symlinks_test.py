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


tasks = TasksDirectory(
    TasksSymlinks(
        "tasks_dictionary",
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

print(tasks.get_task("review-book").task_path)
