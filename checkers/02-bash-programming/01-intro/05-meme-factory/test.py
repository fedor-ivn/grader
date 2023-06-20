import subprocess
import os
import termios


# Define the command to run
cmd = "./solution.sh"


class InteractiveSession:
    def __init__(self, path, args=[]):
        self.master, self.slave = os.openpty()
        old = termios.tcgetattr(self.slave)
        old[3] &= ~termios.ECHO
        termios.tcsetattr(
            self.slave, termios.TCSADRAIN, old
        )

        self.child = subprocess.Popen(
            ["bash", path, *args],
            stdout=self.slave,
            stdin=self.slave,
            stderr=self.slave,
            text=True,
        )
        self.stderr = self.child.stderr
        self.stdout = self.child.stdout

    def health_check(self) -> None:
        pass

    def enter_line(
        self, line: str, add_newline: bool = True
    ) -> None:
        if add_newline:
            line += "\n"
        os.write(self.master, line.encode())

    def expect_output(self, expected_output: str):
        while True:
            line = os.read(self.master, 100).decode("utf-8")

            if line == expected_output:
                return True
            return False

    def check_errors(self):
        return self.child.wait()

    def terminate(self):
        self.child.terminate("123")


class Criterion:
    def __init__(self):
        pass

    def criterion_check(self) -> bool:
        return True


class ResponseCriterion(Criterion):
    def __init__(
        self,
        input_line,
        expected_output,
        session: InteractiveSession,
    ):
        self.input_line = input_line
        self.expected_output = expected_output
        self.session = session

    def criterion_check(self) -> bool:
        self.session.enter_line(self.input_line)
        if self.session.expect_output(self.expected_output):
            return True
        else:
            return False


class ConsoleCriterion(Criterion):
    def __init__(
        self,
        expected_output,
        session: InteractiveSession,
    ):
        self.expected_output = expected_output
        self.session = session

    def criterion_check(self) -> bool:
        if self.session.expect_output(self.expected_output):
            return True
        else:
            return False


class ErrorCriterion(Criterion):
    def __init__(self, session: InteractiveSession):
        self.session = session

    def criterion_check(self) -> bool:
        if session.check_errors() == 0:
            return True
        else:
            return False


class Result:
    def __init__(self, max_score, comment):
        self.score = 0
        self.max_score = max_score
        self.comment = comment

    def maximize_score(self):
        self.score = self.max_score

    def get_score(self):
        return self.score

    def get_comment(self):
        return self.comment


class Test:
    def __init__(self, criterion, result):
        self.criterion = criterion
        self.result = result

    def run(self):
        if self.criterion.criterion_check():
            self.result.maximize_score()

        print(
            f"{self.result.get_comment()} - {self.result.get_score()} баллов"
        )

    def get_score(self):
        return self.result.score


class Test_set:
    def __init__(self, tests: list):
        self.tests = tests

    def add_test(self, test):
        self.tests.append(test)

    def run_all(self):
        for test in self.tests:
            test.run()

        print(f"Итого: {self.get_overall_score()} баллов")

    def get_overall_score(self):
        score = 0
        for test in self.tests:
            score += test.get_score()
        return score


session = InteractiveSession("./solution.sh")

tests_list = [
    Test(
        ConsoleCriterion(
            expected_output="Подпись к мему: ",
            session=session,
        ),
        Result(
            max_score=5,
            comment="Скрипт запрашивает подпись для мема",
        ),
    ),
    Test(
        ResponseCriterion(
            input_line="четыре",
            expected_output="Название файла: ",
            session=session,
        ),
        Result(
            max_score=5,
            comment="Скрипт запрашивает путь выходного файла",
        ),
    ),
    Test(
        ResponseCriterion(
            input_line="test.png",
            expected_output="Мем сохранён!\r\n",
            session=session,
        ),
        Result(
            max_score=5,
            comment="Скрипт выводит сообщение, что мем сохранён",
        ),
    ),
    Test(
        ErrorCriterion(session=session),
        Result(
            max_score=30,
            comment="Скрипт выполняется без ошибок",
        ),
    ),
]

tests = Test_set(tests_list)

tests.run_all()