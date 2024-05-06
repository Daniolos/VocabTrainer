import tkinter as tk
from typing import Type

from controllers.view_controller import ViewController
from models.exercise_model import ExerciseModel


class AppController:
    def __init__(
        self,
        exercise_model: ExerciseModel,
        app: tk.Tk,
        controller: ViewController,
    ) -> None:
        self.exercise_model = exercise_model
        self.app = app

        self.current_controller: ViewController = None
        self.display_view(controller)

    def display_view(self, view_controller: Type[ViewController]):
        if self.current_controller is not None:
            self.current_controller.hide()

        self.current_controller = view_controller(self.app, self)
        self.current_controller.display()

    def run(self):
        self.app.mainloop()
