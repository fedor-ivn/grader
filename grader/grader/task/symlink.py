import os

from grader.source_directory.directory import (
    SourceDirectory,
)


class TaskSymlink:
    def __init__(
        self,
        target_path: str,
        task_source_path: str,
    ):
        self.target_path = target_path
        self.task_source_path = task_source_path

    def task_path(self) -> str:
        """ """
        return f"{self.target_path}/{self.name()}"

    def name(self) -> str:
        """
        Transforms the task source path into the task name.

        Example:
            `checkers/02-bash-programming/01-intro/05-meme-factory`
            would become `meme-factory`

        :return: task name, e.g. "review-book"
        """
        full_name = self.task_source_path.split("/")[-1]
        name = full_name[full_name.find("-") + 1 :]
        return name

    def create(self) -> None:
        """
        Create the symlink to the task source directory.
        """

        name = self.name()
        task_path = self.task_path()

        if os.path.exists(task_path):
            print(f"Symlink {name} already exists")

        else:
            os.symlink(
                self.task_source_path,
                task_path,
            )


class TasksSymlinks:
    def __init__(
        self,
        target_path: str,
        source_directory: SourceDirectory,
    ):
        self.target_path = target_path
        self.source_directory = source_directory

    def healthcheck(self) -> None:
        """
        Checks if the tasks directory is empty. If empty,
        creates the symlinks to tasks source directory.
        """
        if os.path.exists(self.target_path):
            return

        os.makedirs(self.target_path)

        paths = self.source_directory.task_paths()
        for path in paths:
            symlink = TaskSymlink(self.target_path, path)
            symlink.create()
