from abc import ABC
from tmpgrader.output.score.template import ScoreTemplate
from tmpgrader.output.feedback.template import FeedbackTemplate


class Result(ABC):
    def __init__(self, score: ScoreTemplate, feedback: FeedbackTemplate) -> None:
        self.score = score
        self.feedback = feedback

    def result(self, is_passed: bool) -> str:
        return f"Score: {self.score.score(is_passed)}, Feedback: {self.feedback.feedback(is_passed)}"
