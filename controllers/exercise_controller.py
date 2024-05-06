from time import perf_counter
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

        self.view: ExerciseView = ExerciseView(app, self)
        self.reset()

    @property
    def elapsed_time(self):
        return perf_counter() - self.start_time

    @property
    def exercise_container(self):
        return self.app_controller.exercise_model.exercise_container

    def handle_button(self):
        if not self.exercise_container.current_exercise:
            return

        entry = self.view.entry_variable.get()
        return (
            self.handle_correct_entry()
            if self.app_controller.exercise_model.answer_verifier.verify(entry)
            else self.handle_wrong_entry()
        )

    def handle_correct_entry(self):
        self.exercise_container.set_next_exercise()
        self.set_progress()

        return (
            self.display_next_exercise()
            if self.exercise_container.current_exercise
            else self.display_end_view()
        )

    def display_next_exercise(self):
        self.view.set_feedback(f"Correct! ({round(self.elapsed_time, 2)}s)", "#80af23")
        self.view.feedback.after(1_000, lambda: self.view.feedback.set_text(""))
        self.reset()

    def reset(self):
        self.wrong_counter = 0
        self.view.set_assignment(self.exercise_container.current_exercise.assignment)
        self.view.entry_variable.set("")
        self.start_time = perf_counter()

    def display_end_view(self):
        self.view.after(200, lambda: self.app_controller.display_view(EndController))

    def handle_wrong_entry(self):
        self.wrong_counter += 1
        self.set_progress()

        return (
            self.display_lecture_view()
            if self.wrong_counter >= 3
            else self.display_feedback()
        )

    def set_progress(self):
        container = self.exercise_container
        maximum = len(container.exercise_list) + len(container.wrong_exercise_list)
        value = self.determine_progress_value()

        self.view.set_progress_bar(maximum, value)

    def determine_progress_value(self):
        container = self.exercise_container
        if container.current_exercise_list is container.exercise_list:
            return container.current_exercise_index
        if container.current_exercise_list is container.wrong_exercise_list:
            return len(container.exercise_list) + container.current_exercise_index
        return len(container.exercise_list) + len(container.wrong_exercise_list)

    def display_lecture_view(self):
        self.app_controller.display_view(LectureController)

    def display_feedback(self):
        self.exercise_container.mark_exercise_wrong()
        self.view.set_feedback(
            f"Your answer was wrong. Try again! ({round(self.elapsed_time, 2)}s)",
            "#c51e5a",
        )
