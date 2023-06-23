from cli.solution.solution import Solution



# Interface
class TestingSystem:
    def run(self, task: Task, solution: Solution):
        pass

    def submit(self, task: Task, solution: Solution):
        pass

    def text(self, task: Task):
        pass

    def hint(self, task: Task):
        pass
