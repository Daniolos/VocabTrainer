from models.exercise_container import ExerciseContainer
from models.exercise_loader import ExerciseLoader
from models.exercise_verifier import AnswerVerifier


class ExerciseModel:
    def __init__(
        self,
        exercise_loader: ExerciseLoader,
        exercise_container: type[ExerciseContainer],
        answer_verifier: type[AnswerVerifier],
    ):
        exercise_list = exercise_loader.load_exercise_list()

        self.exercise_container = exercise_container(exercise_list)
        self.answer_verifier = answer_verifier(self.exercise_container)
