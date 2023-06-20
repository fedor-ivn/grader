from argparse import ArgumentParser


class CliArgumentParser(ArgumentParser):
    def __init__(self):
        super().__init__(description="Grader CLI")
        super().add_argument("command_name", help="command name")
        super().add_argument("task_name", help="name of the task to grade")
        super().add_argument("solution_path", help="path to the solution file")