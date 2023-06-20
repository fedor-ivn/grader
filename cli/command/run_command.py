from cli.testing_system.testing_system import TestingSystem
from cli.command.user_command import UserCommand


class RunCommand(UserCommand):

    def __init__(self, task: Task, solution: Solution):
        self.task = task
        self.solution = solution

    def execute(self, testing_system: TestingSystem):
        testing_system.run(self.task, self.solution)
