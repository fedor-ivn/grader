class CriterionOutput:
    """
    This is a class which is used to store an output results of a single criterion
    """

    def __init__(self, is_passed: bool, score: int, feedback: str) -> None:
        """
        Initializes a new CriterionOutput instance.

        Attributes:
            is_passed (bool): value containing the boolean result of the criterion.
            score (int): points for the criterion.
            feedback (str): feedback for the criterion
        """
        self._is_passed = is_passed
        self._score = score
        self._feedback = feedback


    def is_passed(self) -> bool:
        """
        Returns the boolean result of the criterion
        """
        return self._is_passed

    def score(self) -> int:
        """
        Returns the score for the criterion
        """
        return self._score

    def feedback(self) -> str:
        """
        Returns the feedback for the criterion
        """
        return self._feedback
