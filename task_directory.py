import os
from more_itertools import flatten


class TaskSymlink:
    # todo: норм так хранить константы?
    TASK_FILES = [
        "test.py",
        "reference-solution.sh",
        # "statement.md",
    ]

    def __init__(self, source_directory, target_path):
        self.source_directory = source_directory
        self.target_path = target_path

    def task_path(self):
        return f"{self.target_path}/{self.name()}"

    def name(self):
        full_name = self.source_directory.split("/")[-1]
        name = full_name[full_name.find("-") + 1 :]
        return name

    # def healthcheck(self):
    #     task_path = self.task_path()
    #     for task_file in self.TASK_FILES:
    #         if not os.path.exists(
    #             f"{task_path}/{task_file}"
    #         ):
    #             raise FileNotFoundError(
    #                 f"File {task_file} not found in task {task_path}"
    #             )

    def create(self):
        # self.healthcheck()

        name = self.name()
        task_path = self.task_path()

        if os.path.exists(task_path):
            print(f"Symlink {name} already exists")
        else:
            os.symlink(
                self.source_directory,
                task_path,
            )


class SourceDirectory:
    def __init__(self, source_tree, depth):
        self.source_tree = source_tree
        self.depth = depth
        pass

    def _traverse_directory(self, path, remaining_depth):
        directories = []
        entries = os.listdir(path)

        for entry in entries:
            entry_path = os.path.join(path, entry)
            if os.path.isdir(entry_path):
                directories.append(entry_path)

        if remaining_depth == 0:
            return directories
        else:
            return list(
                flatten(
                    self._traverse_directory(
                        directory, remaining_depth - 1
                    )
                    for directory in directories
                )
            )

    def task_paths(self):
        return self._traverse_directory(
            self.source_tree, self.depth
        )


class TasksSymlinks:
    def __init__(self, target_path, source_directory):
        self.target_path = target_path
        self.source_directory = source_directory

    def healthcheck(self):
        paths = self.source_directory.task_paths()

        for path in paths:
            symlink = TaskSymlink(path, self.target_path)
            symlink.create()


class TasksDirectory:
    def __init__(self, tasks_path="tasks"):
        self.tasks_path = tasks_path
        tasks_symlinks = TasksSymlinks(
            "tasks", SourceDirectory("checkers", 2)
        )
        tasks_symlinks.healthcheck()

    def is_present(self, task_name):
        return task_name in os.listdir(self.tasks_path)

    def get_task(self, task_name):
        if self.is_present(task_name):
            task_path = f"{self.tasks_path}/{task_name}"
            return Task(task_path)
        else:
            raise KeyError(f"Task {task_name} not found")


class Task:
    def __init__(self, task_path):
        self.task_path = task_path


task = TasksDirectory().get_task("review-book")
