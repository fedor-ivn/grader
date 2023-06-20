import os

from more_itertools import flatten
from source_directory.files_healthcheck import (
    TaskFilesHealthcheck,
)


class SourceDirectory:
    def __init__(
        self,
        source_tree: str,
        depth: int,
        task_files_healthcheck: TaskFilesHealthcheck,
    ):
        self.source_tree = source_tree
        self.depth = depth
        self.task_files_healthcheck = task_files_healthcheck

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
        task_paths = self._traverse_directory(
            self.source_tree, self.depth
        )
        for task_path in task_paths:
            self.task_files_healthcheck.check(task_path)
        return task_paths
