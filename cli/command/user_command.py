from cli.testing_system.testing_system import TestingSystem


# Interface
class UserCommand:

    def execute(self, testing_system: TestingSystem):
        pass
