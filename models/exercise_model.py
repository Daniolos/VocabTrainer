import random
from models.answer import Answer
from models.answer_container import AnswerContainer
from models.exercise import Exercise


class ExerciseModel:
    def __init__(
        self,
        exercise_list: list[Exercise],
        answer_container: AnswerContainer,
    ):
        self.exercise_list = exercise_list
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
        self.current_exercise_list = (
            self.wrong_exercise_list
            if self.current_exercise_list is self.exercise_list
            else None
        )

    def add_answer(self, answer: Answer):
        self.answer_container.add_answer(answer)

    def reset(self):
        self.shuffle_exercise_list()
        self.current_exercise_index = 0
        self.current_exercise_list = self.exercise_list
        self.answer_container.reset()

    def shuffle_exercise_list(self):
        random.shuffle(self.exercise_list)
