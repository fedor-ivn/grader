import importlib
import importlib.util
from grader.criteria.sequential_criteria import SequentialCriteria


class Task:
    def __init__(self, task_path: str):
        self.task_path = task_path

    def criteria(self) -> SequentialCriteria:
        spec = importlib.util.spec_from_file_location(
            "Test", f"{self.task_path}/test.py"
        )
        module = importlib.util.module_from_spec(spec)  # type: ignore
        spec.loader.exec_module(module)  # type: ignore

        criteria = module.criteria

        return criteria  # type: ignore
