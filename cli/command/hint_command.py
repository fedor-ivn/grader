from cli.command.user_command import UserCommand
from cli.task.task import Task
from cli.testing_system.testing_system import TestingSystem


class HintCommand(UserCommand):

    def __init__(self, task: Task):
        self.task = task

    def execute(self, testing_system: TestingSystem):
        testing_system.hint(self.task)
