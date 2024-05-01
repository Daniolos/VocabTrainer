import tkinter as tk

from controllers.protocols.start_controller_protocol import StartControllerProtocol
from views.widgets import Label, SubmitButton
from app import App


class StartView(tk.Frame):
    def __init__(self, master: App, controller: StartControllerProtocol):
        super().__init__(master, padx=200, pady=200)

        Label(self, text="Please Provide a vocabulary.json")

        SubmitButton(
            self,
            text="Next Frame",
            command=lambda: controller.start_exercise(),
        )
