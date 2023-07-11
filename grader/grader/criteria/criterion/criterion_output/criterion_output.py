class CriterionOutput:
    """
    This is a class which is used to store an output results of a single criterion
    """

    def __init__(self, is_passed: bool, score: int, feedback: str) -> None:
        self._is_passed = is_passed
        self._score = score
        self._feedback = feedback

    def is_passed(self) -> bool:
        return self._is_passed

    def score(self) -> int:
        return self._score

    def feedback(self) -> str:
        return self._feedback
