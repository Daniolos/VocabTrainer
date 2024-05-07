from app import App
from app_controller import AppController
from controllers.exercise_controller import ExerciseController
from models.answer_container import AnswerContainer
from models.exercise_loader import ExerciseLoader
from models.exercise_model import ExerciseModel
from models.exercise_verifier import AnswerVerifier


def main():
    loader = ExerciseLoader("vocabularies/test.json")
    exercise_list = loader.load_exercise_list()

    answer_container = AnswerContainer()
    exercise_model = ExerciseModel(exercise_list, answer_container)
    answer_verifier = AnswerVerifier()
    app = App()

    app_controller = AppController(
        exercise_model,
        answer_verifier,
        app,
        ExerciseController,
    )
    app_controller.run()


if __name__ == "__main__":
    main()
