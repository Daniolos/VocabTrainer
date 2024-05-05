from app import App
from controllers.view_controller import ViewController
from views.lecture_view import LectureView


class LectureController(ViewController):
    def __init__(self, app: App) -> None:
        self.app = app

        self.view = LectureView(app, self, app.vocab_model.current_vocab)

    def handle_button(self):
        from controllers.exercise_controller import ExerciseController

        self.app.display_view(ExerciseController)
