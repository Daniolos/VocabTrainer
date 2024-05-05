from controllers.exercise_controller import ExerciseController
from models import VocabModel
from app import App


def main():
    vocab_model = VocabModel("vocabularies/unit4.json")

    app = App(vocab_model, ExerciseController)
    app.run()


if __name__ == "__main__":
    main()
