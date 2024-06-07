from dataclasses import dataclass
import json
from pathlib import Path
import random

from models.exercise import Exercise


@dataclass
class ExerciseLoader:
    def load_exercise_lists(
        self, path: str = "vocabularies", pattern: str = "*.json"
    ) -> list[list[Exercise]]:
        return [self.load_exercise_list(path) for path in Path(path).glob(pattern)]

    def load_exercise_list(self, path: Path) -> list[Exercise]:
        with open(path, "r", encoding="utf-8") as file:
            exercise_data_list = json.load(file)

        if not self.validate_format(exercise_data_list):
            raise Exception(
                "The provided JSON data has not a valid format. "
                "Please read the README.md for more information."
            )

        exercise_list = [
            Exercise(exercise_data) for exercise_data in exercise_data_list
        ]
        random.shuffle(exercise_list)

        return exercise_list

    @staticmethod
    def validate_format(data) -> bool:
        if not isinstance(data, list):
            return False
        for item in data:
            if not isinstance(item, dict):
                return False
            if not all(key in item.keys() for key in ["assignment", "solution"]):
                return False
            if not all(isinstance(value, str) for value in item.values()):
                return False
        return True
