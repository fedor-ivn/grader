from cli.solution.solution import Solution
from cli.testing_system.testing_system import TestingSystem
from task_directory import Task


class CommandLineTestingSystem(TestingSystem):

    def __init__(self):
        super().__init__()

    def run(self, task: Task, solution: Solution):
        pass

    def submit(self, task: Task, solution: Solution):
        pass

    def text(self, task: Task):
        pass

    def hint(self, task: Task):
        pass
