from dataclasses import dataclass
import json
import random

from models.exercise import Exercise


@dataclass
class ExerciseLoader:
    file_name: str

    def load_exercise_list(self) -> list[Exercise]:
        with open(self.file_name, "r", encoding="utf-8") as file:
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
