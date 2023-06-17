import subprocess
from interactive_bash import main

file = "./solution.sh"


class InteractiveSession:
    def __init__(self, path, args=[]):
        self.child = subprocess.Popen(
            ["bash", path, *args],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
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
        output, errors = self.child.communicate()
        print(output, errors)

        if output == expected_output:
            print("Вывод совпадает с требованиями")
            return True

        else:
            return False

    def terminate(self):
        self.child.terminate()


session = InteractiveSession(file)

if session.expect_output("Мем сохранён!\n"):
    print("+")
else:
    print("-")
session.enter_line("Пример")
session.enter_line("example.jpg")
