from dataclasses import dataclass

from models.exercise import Exercise


@dataclass
class Answer:
    value: str
    exercise: Exercise
    seconds_needed: float
    is_correct: bool
