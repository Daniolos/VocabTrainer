import tkinter as tk

from app import App
from controllers.protocols.exercise_controller_protocol import (
    ExerciseControllerProtocol,
)
from models.exercise import Exercise
from views.widgets import Label, SubmitButton


class LectureView(tk.Frame):

    def __init__(
        self, master: App, controller: ExerciseControllerProtocol, exercise: Exercise
    ):
        super().__init__(master, padx=200, pady=200)

        Label(self, f"The correct answer for {exercise.assignment} is")
        Label(self, exercise.solution)

        self.button = SubmitButton(
            self,
            text="Return",
            command=lambda: controller.handle_button(),
        )
