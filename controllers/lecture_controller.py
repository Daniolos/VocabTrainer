from app import App
from app_controller import AppController
from controllers.view_controller import ViewController
from views.lecture_view import LectureView


class LectureController(ViewController):
    def __init__(self, app: App, app_controller: AppController) -> None:
        self.app = app
        self.app_controller = app_controller

        self.view = LectureView(
            app, self, app_controller.exercise_model.current_exercise
        )

    def handle_button(self):
        from controllers.exercise_controller import ExerciseController

        self.app_controller.display_view(ExerciseController)
