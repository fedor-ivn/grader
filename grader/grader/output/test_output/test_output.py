from abc import ABC


class TestOutput(ABC):
    def __init__(self, score: int, feedback: str) -> None:
        self.score = score
        self.feedback = feedback

    def output(self) -> str:
        return f"Results:\n{self.feedback}\nOverall score: {self.score}"
