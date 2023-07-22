from abc import ABC


class Feedback(ABC):
    """
    The class which represents a feedback which will be given to
    the user after the solution evaluation
    """

    def __init__(
        self, positive: str, negative: str
    ) -> None:
        """
        Creates a new instance of the Feedback class

        Attributes:
            positive (str): a feedback for the correct solution
            negative (str): a feedback for the incorrect solution
        """
        self.positive = positive
        self.negative = negative

    def feedback(self, is_passed: bool) -> str:
        """
        Provides a corresponding feedback

        Args:
            is_passed (bool): whether the criteria was passed or not
        """
        if is_passed:
            return self.positive
        return self.negative
