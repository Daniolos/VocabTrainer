import random
from models.answer import Answer
from models.answer_container import AnswerContainer
from models.exercise import Exercise


class ExerciseModel:
    def __init__(
        self,
        exercise_lists: list[list[Exercise]],
        answer_container: AnswerContainer,
    ):
        self.exercise_lists = exercise_lists
        self.answer_container = answer_container

        self.reset()

    @property
    def current_exercise(self):
        return (
            self.current_exercise_list[self.current_exercise_index]
            if self.current_exercise_list
            else None
        )

    @property
    def current_exercise_list(self):
        if self.current_exercise_list_index < len(self.exercise_lists):
            return self.exercise_lists[self.current_exercise_list_index]
        if self.current_exercise_list_index == len(self.exercise_lists):
            return self.wrong_exercise_list
        return None

    @property
    def is_last_exercise(self):
        return self.current_exercise_index >= len(self.current_exercise_list) - 1

    @property
    def wrong_exercise_list(self):
        return self.answer_container.wrong_exercise_list

    def set_next_exercise(self):
        if not self.is_last_exercise:
            self.current_exercise_index += 1
        else:
            self.current_exercise_index = 0
            self.set_next_list()

    def set_next_list(self):
        self.current_exercise_list_index += 1

    def add_answer(self, answer: Answer):
        self.answer_container.add_answer(answer)

    def reset(self):
        self.shuffle_exercise_lists()
        self.current_exercise_index = 0
        self.current_exercise_list_index = 0
        self.answer_container.reset()

    def shuffle_exercise_lists(self):
        for exercise_list in self.exercise_lists:
            random.shuffle(exercise_list)
