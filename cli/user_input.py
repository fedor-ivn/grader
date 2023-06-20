from argparse import ArgumentParser

from cli.command.hint_command import HintCommand
from cli.command.run_command import RunCommand
from cli.command.submit_command import SubmitCommand
from cli.command.text_command import TextCommand
from cli.command.user_command import UserCommand
from cli.solution.solution_of import SolutionOf
from cli.task.task_of import TaskOf


class UserInput:
    def __init__(self, argument_parser: ArgumentParser):
        self.argument_parser = argument_parser

    def get_command(self) -> UserCommand:
        args = self.argument_parser.parse_args()
        if args.command_name == "run":
            return RunCommand(
                TaskOf(args.task_name),
                SolutionOf(args.solution_path),
            )
        elif args.command_name == "submit":
            return SubmitCommand(
                TaskOf(args.task_name),
                SolutionOf(args.solution_path),
            )
        elif args.command_name == "text":
            return TextCommand(TaskOf(args.task_name))
        elif args.command_name == "hint":
            return HintCommand(TaskOf(args.task_name))
