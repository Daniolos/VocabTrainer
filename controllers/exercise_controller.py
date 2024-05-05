from app import App
from app_controller import AppController
from controllers.end_controller import EndController
from controllers.lecture_controller import LectureController
from controllers.view_controller import ViewController
from controllers.protocols.exercise_controller_protocol import (
    ExerciseControllerProtocol,
)
from views.exercise_view import ExerciseView


class ExerciseController(ViewController, ExerciseControllerProtocol):
    def __init__(self, app: App, app_controller: AppController) -> None:
        self.app = app
        self.app_controller = app_controller

        self.wrong_counter = 0

        vocab = self.app_controller.vocab_model.current_vocab
        self.view: ExerciseView = ExerciseView(app, self, vocab)

    def handle_button(self):
        entry = self.view.entry_variable.get()
        return (
            self.handle_correct_entry()
            if self.app_controller.vocab_model.verify_input(entry)
            else self.handle_wrong_entry()
        )

    def handle_correct_entry(self):
        return (
            self.display_next_vocab()
            if self.app_controller.vocab_model.next_vocab
            else self.display_end_view()
        )

    def set_progress(self):
        maximum = len(self.app_controller.vocab_model.vocab_list) + len(
            self.app_controller.vocab_model.wrong_vocab_list
        )
        vocab_model = self.app_controller.vocab_model
        value = (
            vocab_model.current_vocab_index
            if vocab_model.current_vocab_list is vocab_model.vocab_list
            else len(vocab_model.vocab_list) + vocab_model.current_vocab_index
        )

        self.view.set_progress_bar(maximum, value)

    def display_next_vocab(self):
        self.app_controller.vocab_model.set_next_vocab()
        vocab = self.app_controller.vocab_model.current_vocab
        self.wrong_counter = 0

        self.set_progress()
        self.view.set_vocab(vocab.german)
        self.view.entry_variable.set("")
        self.view.set_feedback("Correct!", "#80af23")
        self.view.feedback.after(1_000, lambda: self.view.feedback.set_text(""))

    def display_end_view(self):
        self.app_controller.display_view(EndController)

    def handle_wrong_entry(self):
        self.wrong_counter += 1
        self.set_progress()

        return (
            self.display_lecture_view()
            if self.wrong_counter >= 3
            else self.display_feedback()
        )

    def display_lecture_view(self):
        self.app_controller.display_view(LectureController)

    def display_feedback(self):
        self.app_controller.vocab_model.mark_vocab_wrong()
        self.view.set_feedback("Your answer was wrong. Try again!", "#c51e5a")
