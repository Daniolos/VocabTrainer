from app import App
from app_controller import AppController
from controllers.exercise_controller import ExerciseController
from models import VocabModel


def main():
    vocab_model = VocabModel("vocabularies/unit4.json")
    app = App()

    app_controller = AppController(vocab_model, app, ExerciseController)
    app_controller.run()


if __name__ == "__main__":
    main()
