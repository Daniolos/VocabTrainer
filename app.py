import tkinter as tk
from typing import Type

from controllers.view_controller import ViewController
from models import VocabModel


class App(tk.Tk):
    def __init__(self, vocab_model: VocabModel, controller: ViewController) -> None:
        super().__init__()
        self.geometry(f"{800}x{600}")
        self.state = False

        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.end_fullscreen)

        self.vocab_model = vocab_model
        self.current_controller: ViewController = None
        self.display_view(controller)

    def toggle_fullscreen(self, event=None):
        self._set_fullscreen(not self.state)

    def end_fullscreen(self, event=None):
        self._set_fullscreen(False)

    def _set_fullscreen(self, state):
        self.state = state
        self.attributes("-fullscreen", state)

    def display_view(self, view_controller: Type[ViewController]):
        if self.current_controller is not None:
            self.current_controller.hide()

        self.current_controller = view_controller(self)
        self.current_controller.display()

    def run(self):
        self.mainloop()
