import tkinter as tk

from app import App
from controllers.protocols.exercise_controller_protocol import (
    ExerciseControllerProtocol,
)
from models.exercise import Exercise
from views.widgets import Entry, Label, ProgressBar, SubmitButton


class ExerciseView(tk.Frame):

    def __init__(self, master: App, controller: ExerciseControllerProtocol):
        super().__init__(master, padx=200, pady=200)

        self.progress_bar = ProgressBar(self, 0, 0)

        Label(self, "Translate the following vocabulary")
        self.assignment = Label(self)
        self.entry_variable = tk.StringVar()

        entry = Entry(self, self.entry_variable)
        entry.bind("<Return>", lambda _: controller.handle_button())

        self.feedback = Label(self)

        self.button = SubmitButton(
            self,
            text="Submit",
            command=lambda: controller.handle_button(),
        )

    def set_assignment(self, text: str) -> None:
        self.assignment.set_text(text)

    def set_feedback(self, text: str, foreground: str) -> None:
        self.feedback.set_text(text, foreground)

    def set_progress_bar(self, maximum, value):
        self.progress_bar.config(maximum=maximum, value=value)
