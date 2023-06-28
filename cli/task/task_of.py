from cli.task.task import Task


class TaskOf(Task):
    def __init__(self, path: str):
        super().__init__(path)
