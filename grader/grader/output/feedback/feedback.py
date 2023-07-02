from abc import ABC


class Feedback(ABC):
    def __init__(
        self, positive: str, negative: str
    ) -> None:
        self.positive = positive
        self.negative = negative

    def feedback(self, is_passed: bool) -> str:
        if is_passed:
            return self.positive
        return self.negative
