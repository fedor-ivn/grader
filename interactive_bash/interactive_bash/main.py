import shutil
import subprocess
import asyncio
import sys
import os


HELP = """Доступные команды:

  help         - вывести справку по командам
  add-review   - добавить отзыв
  list-reviews - показать все отзывы
  clear        - удалить все отзывы
"""


class InteractiveSession:
    def __init__(self, path, args=[]):
        bash_executable = shutil.which("bash")
        self.child = subprocess.Popen(
            [bash_executable, path, *args],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.stdout = self.child.stdout
        self.stderr = self.child.stderr

    def health_check(self):
        pass

    def enter_line(self, line: str, add_newline=True):
        if add_newline:
            line += "\n"
        self.child.stdin.write(line)
        self.child.stdin.flush()

    def expect_output(self, expected_output: str):
        while True:
            line = self.child.stdout.readline()
            print(line)
            # if not line:
            #     raise Exception(
            #         f'Expected output "{expected_output}", but process ended without producing it.'
            #     )
            if line == expected_output:
                return
        expected_lines = expected_output.split("\n")
        for expected_line in expected_lines:
            try:
                line, errs = self.child.stdout.communicate(
                    timeout=15
                )
            except subprocess.TimeoutExpired:
                self.child.kill()

            if line != expected_line:
                raise Exception(
                    f'Expected line $"{expected_line}", but reached end of output'
                )
            assert line == expected_line

    def terminate(self):
        self.child.terminate()


def main():
    solution = InteractiveSession(path="solution.sh")
    try:
        solution.enter_line("help")
        solution.expect_output(HELP)
    finally:
        solution.terminate()


if __name__ == "__main__":
    main()
