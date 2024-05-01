from controllers.start_controller import StartController
from models import VocabModel
from app import App


def main():
    vocab_model = VocabModel("vocabularies/unit4.json")

    app = App(vocab_model, StartController)
    app.run()


if __name__ == "__main__":
    main()
