from dataclasses import dataclass
import re

from models.exercise_container import ExerciseContainer


@dataclass
class AnswerVerifier:
    exercise_container: ExerciseContainer

    def verify(self, input: str) -> bool:
        return (
            True
            if self.comparable(input)
            == self.comparable(self.exercise_container.current_exercise.solution)
            else False
        )

    @staticmethod
    def comparable(text: str) -> list[str]:
        text = re.sub(r"\([^\)]*\)", "", text)
        return (
            text.replace("to ", "")
            .replace("the ", "")
            .replace("a ", "")
            .replace("be ", "")
            .replace("sb.", "somebody")
            .replace("someone", "somebody")
            .strip()
        )
