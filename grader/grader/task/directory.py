import os
from grader.task.symlink import TasksSymlinks
from grader.task.task import Task


class TasksDirectory:
    def __init__(self, tasks_symlinks: TasksSymlinks):
        self.symlinks = tasks_symlinks

    def is_present(self, task_name: str) -> bool:
        """
        Check if task is present in the symlinked tasks
        """
        return task_name in os.listdir(
            self.symlinks.target_path
        )

    def get_task(self, task_name: str) -> Task:
        """
        Get task by name from the symlinked tasks
        directory. Additionally, performs healthcheck.

        return: Task if found
        throws: KeyError if not found
        """
        self.symlinks.healthcheck()

        if self.is_present(task_name):
            task_path = (
                f"{self.symlinks.target_path}/{task_name}"
            )
            return Task(task_path)
        else:
            raise KeyError(f"Task {task_name} not found")
