from app import App
from app_controller import AppController
from controllers.exercise_controller import ExerciseController
from models.exercise_container import ExerciseContainer
from models.exercise_loader import ExerciseLoader
from models.exercise_model import ExerciseModel
from models.exercise_verifier import AnswerVerifier


def main():
    loader = ExerciseLoader("vocabularies/test.json")
    vocab_model = ExerciseModel(loader, ExerciseContainer, AnswerVerifier)
    app = App()

    app_controller = AppController(vocab_model, app, ExerciseController)
    app_controller.run()


if __name__ == "__main__":
    main()
