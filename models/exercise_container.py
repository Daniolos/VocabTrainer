import random
from models.exercise import Exercise


class ExerciseContainer:
    def __init__(self, exercise_list: list[Exercise]):
        self.exercise_list = exercise_list
        self.reset()

    @property
    def current_exercise(self):
        return (
            self.current_exercise_list[self.current_exercise_index]
            if self.current_exercise_list
            else None
        )

    @property
    def next_exercise(self):
        if self.is_last_exercise:
            return self.next_list[0] if self.next_list else None

        index = self.current_exercise_index + 1
        return self.current_exercise_list[index]

    @property
    def is_last_exercise(self):
        return self.current_exercise_index >= len(self.current_exercise_list) - 1

    @property
    def next_list(self):
        return (
            self.wrong_exercise_list
            if self.current_exercise_list is self.exercise_list
            else None
        )

    def set_next_exercise(self):
        if not self.is_last_exercise:
            self.current_exercise_index += 1
        else:
            self.current_exercise_index = 0
            self.set_next_list()

    def set_next_list(self):
        self.current_exercise_list = self.next_list

    def mark_exercise_wrong(self):
        if self.current_exercise in self.wrong_exercise_list:
            return
        self.wrong_exercise_list.append(self.current_exercise)

    def reset(self):
        self.shuffle_exercise_list()
        self.wrong_exercise_list: list[Exercise] = []
        self.current_exercise_index = 0
        self.current_exercise_list = self.exercise_list

    def shuffle_exercise_list(self):
        random.shuffle(self.exercise_list)
