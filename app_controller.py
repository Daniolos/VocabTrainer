import tkinter as tk
from typing import Type

from controllers.view_controller import ViewController
from models import VocabModel


class AppController:
    def __init__(
        self,
        vocab_model: VocabModel,
        app: tk.Tk,
        controller: ViewController,
    ) -> None:
        self.vocab_model = vocab_model
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
