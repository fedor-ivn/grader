import importlib
import importlib.util
from grader.tests.test import TestTemplate


class Task:
    def __init__(self, task_path: str):
        self.task_path = task_path

    def create_test(self) -> TestTemplate:
        spec = importlib.util.spec_from_file_location(
            "Test", f"{self.task_path}/test.py"
        )
        module = importlib.util.module_from_spec(spec)  # type: ignore
        spec.loader.exec_module(module)  # type: ignore

        test = module.__dict__["Test"]()

        return test  # type: ignore
