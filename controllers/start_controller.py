from app import App
from controllers.exercise_controller import ExerciseController
from controllers.protocols.start_controller_protocol import StartControllerProtocol
from controllers.view_controller import ViewController
from views.start_view import StartView


class StartController(ViewController, StartControllerProtocol):
    def __init__(self, app: App) -> None:
        self.app = app

        self.view = StartView(app, self)

    def start_exercise(self):
        self.app.display_view(ExerciseController)
