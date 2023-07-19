from grader.ibash.ibash import IBash
from grader.output.test_output.test_output import TestOutput
from grader.criteria.sequential_criteria import SequentialCriteria


class Test():
    def __init__(self, criteria: SequentialCriteria) -> None:
        self._criteria = criteria

    def output(self, solution: IBash) -> str:
        test_output: TestOutput
        test_output = self._criteria.test(
            solution.start_session()
        )
        return test_output.output()
