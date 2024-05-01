import tkinter as tk

from app import App
from controllers.protocols.exercise_controller_protocol import (
    ExerciseControllerProtocol,
)
from models import Vocab
from views.widgets import Entry, Label, SubmitButton


class ExerciseView(tk.Frame):

    def __init__(
        self, master: App, controller: ExerciseControllerProtocol, vocab: Vocab
    ):
        super().__init__(master, padx=200, pady=200)

        Label(self, "Translate the following vocabulary")
        self.vocab = Label(self, vocab.german)
        self.entry_variable = tk.StringVar()

        entry = Entry(self, self.entry_variable)
        entry.bind("<Return>", lambda _: controller.handle_button())

        self.feedback = Label(self, "")

        self.button = SubmitButton(
            self,
            text="Submit",
            command=lambda: controller.handle_button(),
        )

    def set_vocab(self, text: str) -> None:
        self.vocab.config(text=text)

    def set_feedback(self, text: str, foreground: str) -> None:
        self.feedback.config(text=text, foreground=foreground)
