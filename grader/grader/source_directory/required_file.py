from abc import ABC, abstractmethod


class TaskFile(ABC):
    @abstractmethod
    def name(self) -> str:
        pass


class TaskFileTestPy(TaskFile):
    def name(self) -> str:
        return "test.py"


class TaskFileGitkeep(TaskFile):
    def name(self) -> str:
        return ".gitkeep"


class TaskFileReferenceSolutionSh(TaskFile):
    def name(self) -> str:
        return "reference-solution.sh"


class TaskFileStatementMd(TaskFile):
    def name(self) -> str:
        return "statement.md"
