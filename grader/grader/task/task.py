class Task:
    def __init__(self, task_path: str):
        self.task_path = task_path

    def exec_import(self) -> None:
        exec(
            f"from tasks_directory.{self.task_path} import Test"
        )
