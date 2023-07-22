from abc import ABC


class Score(ABC):
    """
    This class represents a points which user gets for the passed
    or not passed criterion.
    """

    def __init__(self, max_score: int) -> None:
        """
        Creates a new Score instance.

        Attributes:
            max_score (int): the maximum points for the criterion.
        """
        self.max_score = max_score

    def score(self, is_passed: bool) -> int:
        """
        Returns the points for the criterion.

        Args:
            is_passed (bool): Whether the criterion was passed or not.
        """
        if is_passed:
            return self.max_score
        return 0
