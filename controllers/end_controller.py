from app import App
from app_controller import AppController
from controllers.protocols.end_controller_protocol import EndControllerProtocol
from controllers.view_controller import ViewController
from views.end_view import EndView


class EndController(ViewController, EndControllerProtocol):
    def __init__(self, app: App, app_controller: AppController) -> None:
        self.app = app
        self.app_controller = app_controller

        wrong_answers = ", ".join(
            exercise.solution
            for exercise in self.app_controller.exercise_model.exercise_container.wrong_exercise_list
        )

        self.view = EndView(app, self, wrong_answers)

    def handle_button(self):
        from controllers.exercise_controller import ExerciseController

        self.app_controller.exercise_model.exercise_container.reset()
        self.app_controller.display_view(ExerciseController)
