from app import App
from controllers.lecture_controller import LectureController
from controllers.view_controller import ViewController
from controllers.protocols.exercise_controller_protocol import (
    ExerciseControllerProtocol,
)
from views.exercise_view import ExerciseView


class ExerciseController(ViewController, ExerciseControllerProtocol):
    def __init__(self, app: App) -> None:
        self.app = app

        self.wrong_counter = 0

        vocab = self.app.vocab_model.current_vocab
        self.view: ExerciseView = ExerciseView(app, self, vocab)

    def handle_button(self):
        entry = self.view.entry_variable.get()
        return (
            self.display_next_vocab()
            if self.app.vocab_model.verify_input(entry)
            else self.handle_wrong_entry()
        )

    def display_next_vocab(self):
        self.app.vocab_model.set_next_vocab()
        vocab = self.app.vocab_model.current_vocab
        self.view.set_vocab(vocab.german)
        self.view.entry_variable.set("")
        self.view.set_feedback("Your answer was correct!", "#80af23")

    def handle_wrong_entry(self):
        self.wrong_counter += 1

        return (
            self.display_lecture_view()
            if self.wrong_counter >= 3
            else self.display_feedback()
        )

    def display_lecture_view(self):
        self.wrong_counter == 0
        self.app.display_view(LectureController)

    def display_feedback(self):
        self.app.vocab_model.mark_vocab_wrong()
        self.view.set_feedback("Your answer was wrong. Try again!", "#c51e5a")
