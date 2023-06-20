from cli.command.user_command import UserCommand
from cli.solution.solution import Solution
from cli.task.task import Task
from cli.testing_system.testing_system import TestingSystem


class SubmitCommand(UserCommand):

    def __init__(self, task: Task, solution: Solution):
        self.task = task
        self.solution = solution

    def execute(self, testing_system: TestingSystem):
        testing_system.submit(self.task, self.solution)