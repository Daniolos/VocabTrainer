from app import App
from app_controller import AppController
from controllers.protocols.end_controller_protocol import EndControllerProtocol
from controllers.view_controller import ViewController
from views.end_view import EndView
from views.widgets import TableView


class EndController(ViewController, EndControllerProtocol):
    def __init__(self, app: App, app_controller: AppController) -> None:
        self.app = app
        self.app_controller = app_controller

        wrong_answers = ", ".join(
            f"{answer.value} != {answer.exercise.solution}"
            for answer in self.app_controller.exercise_model.answer_container.wrong_answer_list
        )

        self.view = EndView(
            app,
            self,
            self.app_controller.exercise_model.answer_container.answer_list,
            wrong_answers,
        )

    def handle_button(self):
        from controllers.exercise_controller import ExerciseController

        self.app_controller.exercise_model.reset()
        self.app_controller.display_view(ExerciseController)
