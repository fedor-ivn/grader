from abc import ABC


class TestOutput(ABC):
    """
    This class represents the overall output of the test.
    """

    def __init__(self, score: int, feedback: str) -> None:
        """
        Initializes the new TestOutput instance.

        Attributes:
            score (int): the overall score of the test.
            feedback (str): the compilation of the feedbacks for critera.
        """
        self.score = score
        self.feedback = feedback

    def output(self) -> str:
        """
        Returns the final output of the test.
        """
        return f"Results:\n{self.feedback}\nOverall score: {self.score}"
