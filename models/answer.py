from dataclasses import dataclass

from models.exercise import Exercise


@dataclass
class Answer:
    value: str
    exercise: Exercise
    seconds_needed: float
    is_correct: bool

    def __hash__(self) -> int:
        return hash(self.exercise)

    def __eq__(self, other):
        return isinstance(other, Answer) and self.exercise == other.exercise
