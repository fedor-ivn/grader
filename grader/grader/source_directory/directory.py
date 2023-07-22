import os

from more_itertools import flatten
from grader.source_directory.files_healthcheck import (
    TaskFilesHealthcheck,
)


class SourceDirectory:
    def __init__(
        self,
        source_tree: str,
        task_files_healthcheck: TaskFilesHealthcheck,
        depth: int,
    ):
        self.source_tree = source_tree
        self.task_files_healthcheck = task_files_healthcheck
        self.depth = depth

    def _traverse_directory(
        self, path: str, remaining_depth: int
    ) -> list[str]:
        """
        Recursive function to traverse the source
        directory till some depth level.
        """
        directories = []
        entries = os.listdir(path)

        for entry in entries:
            entry_path = os.path.join(path, entry)
            if os.path.isdir(entry_path):
                directories.append(entry_path)

        if remaining_depth == 0:
            return directories
        else:
            return list(
                flatten(
                    self._traverse_directory(
                        directory, remaining_depth - 1
                    )
                    for directory in directories
                )
            )

    def task_paths(self) -> list[str]:
        """
        Get all task directories in the source
        tree till some depth level.
        """

        return [
            task_path
            for task_path in self._traverse_directory(
                self.source_tree, self.depth
            )
            if self.task_files_healthcheck.check(
                task_path, raise_exception=False
            )
        ]
