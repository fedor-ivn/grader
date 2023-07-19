import os


class ActiveTasks:
    def __init__(
        self, target_path: str, all_tasks: list[str]
    ) -> None:
        self._target_path = target_path
        self._all_tasks = all_tasks

    def active_tasks_list(self) -> list[str]:
        tasks = []
        test_name = "test.py"

        for task in self._all_tasks:
            task_path = os.path.join(
                self._target_path, task
            )
            test_path = os.path.join(task_path, test_name)

            if os.path.isfile(test_path):
                tasks.append(task)

        return tasks
