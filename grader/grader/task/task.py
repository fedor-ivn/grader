import importlib
import importlib.util
from grader.criteria.sequential_criteria import (
    SequentialCriteria,
)
from grader.ibash.ibash import IBash
from grader.output.test_output.test_output import TestOutput


class Task:
    def __init__(self, task_path: str):
        self.task_path = task_path

    def name(self) -> str:
        return self.task_path.split("/")[-1]

    def criteria(self) -> SequentialCriteria:
        spec = importlib.util.spec_from_file_location(
            "Test", f"{self.task_path}/test.py"
        )
        module = importlib.util.module_from_spec(spec)  # type: ignore
        spec.loader.exec_module(module)  # type: ignore

        criteria = module.criteria

        return criteria  # type: ignore

    def output(self, solution: IBash) -> str:
        test_output: TestOutput
        test_output = self.criteria().test(
            solution.start_session()
        )
        return test_output.output()
