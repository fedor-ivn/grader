import os
from source_directory.required_file import TaskFile


class TaskFilesHealthcheck:
    def __init__(self, task_files: list[TaskFile]):
        self.task_files = task_files

    def check(
        self,
        task_source_path: str,
        raise_exception: bool = True,
    ) -> bool:
        """
        Check if all the required task files exist
        in the source directory.

        return: True if all files are present, otherwise False
        trhows: FileNotFoundError if raise_exception is True
                and any of the files is missing
        """

        for task_file in self.task_files:
            if os.path.exists(
                f"{task_source_path}/{task_file.name()}"
            ):
                continue
            if raise_exception:
                raise FileNotFoundError(
                    f"File `{task_file.name()}` not found in task {task_source_path}"
                )
            else:
                return False
        return True
