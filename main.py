from app import App
from app_controller import AppController
from controllers.exercise_controller import ExerciseController
from models.answer_container import AnswerContainer
from models.exercise_loader import ExerciseLoader
from models.exercise_model import ExerciseModel
from models.exercise_verifier import AnswerVerifier


def main():
    loader = ExerciseLoader()
    exercise_lists = loader.load_exercise_lists(pattern="test.json")

    answer_container = AnswerContainer()

    app_controller = AppController(
        ExerciseModel(exercise_lists[0], answer_container),
        AnswerVerifier(),
        App(),
        ExerciseController,
    )
    app_controller.run()


if __name__ == "__main__":
    main()
