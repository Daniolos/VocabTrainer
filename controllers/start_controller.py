from app import App
from app_controller import AppController
from controllers.exercise_controller import ExerciseController
from controllers.protocols.start_controller_protocol import StartControllerProtocol
from controllers.view_controller import ViewController
from views.start_view import StartView


class StartController(ViewController, StartControllerProtocol):
    def __init__(self, app: App, app_controller: AppController) -> None:
        self.app = app
        self.app_controller = app_controller

        self.view = StartView(app, self)

    def start_exercise(self):
        self.app_controller.display_view(ExerciseController)
