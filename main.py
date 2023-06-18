from cli.cli_argument_parser import CliArgumentParser
from cli.testing_system.command_line_testing_system import CommandLineTestingSystem
from cli.user_input import UserInput

if __name__ == "__main__":
    UserInput(CliArgumentParser())\
        .get_command().execute(CommandLineTestingSystem())
