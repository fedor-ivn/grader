from cli.command.user_command import UserCommand
from cli.testing_system.testing_system import TestingSystem


class TextCommand(UserCommand):
    def __init__(self, task: Task):
        self.task = task

    def execute(self, testing_system: TestingSystem):
        testing_system.text(self.task)
