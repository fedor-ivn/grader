import importlib
import importlib.util
from grader.task.directory import TasksDirectory
from grader.tests.test import TestTemplate


class TaskGrader:
    def __init__(
        self, tasks_directory: TasksDirectory
    ) -> None:
        self.tasks_directory = tasks_directory

    def grader_object(self, task_name: str) -> TestTemplate:
        task = self.tasks_directory.get_task(task_name)
        spec = importlib.util.spec_from_file_location(
            "Test", f"{task.task_path}/test.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        test = module.__dict__["Test"]()

        return test
