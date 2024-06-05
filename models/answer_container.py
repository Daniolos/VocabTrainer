from models.answer import Answer
from models.exercise import Exercise


class AnswerContainer:
    def __init__(self) -> None:
        self.reset()

    @property
    def wrong_answer_list(self) -> list[Answer]:
        return [answer for answer in self.answer_list if not answer.is_correct]

    @property
    def wrong_exercise_list(self) -> list[Exercise]:
        return [answer.exercise for answer in set(self.wrong_answer_list)]

    def reset(self):
        self.answer_list: list[Answer] = []

    def add_answer(self, answer: Answer):
        self.answer_list.append(answer)
