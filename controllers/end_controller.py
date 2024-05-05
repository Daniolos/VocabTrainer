from app import App
from app_controller import AppController
from controllers.protocols.end_controller_protocol import EndControllerProtocol
from controllers.view_controller import ViewController
from views.end_view import EndView


class EndController(ViewController, EndControllerProtocol):
    def __init__(self, app: App, app_controller: AppController) -> None:
        self.app = app
        self.app_controller = app_controller

        wrong_vocabs = ", ".join(
            vocab.english for vocab in self.app_controller.vocab_model.wrong_vocab_list
        )

        self.view = EndView(app, self, wrong_vocabs)

    def handle_button(self):
        from controllers.exercise_controller import ExerciseController

        self.app_controller.vocab_model.reset()
        self.app_controller.display_view(ExerciseController)
