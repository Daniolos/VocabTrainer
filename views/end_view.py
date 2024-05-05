import tkinter as tk

from controllers.protocols.end_controller_protocol import EndControllerProtocol
from app import App
from views.widgets import Label, SubmitButton


class EndView(tk.Frame):
    def __init__(self, app: App, controller: EndControllerProtocol, wrong_vocabs: str):
        self.controller = controller

        super().__init__(app, padx=200, pady=200)
        Label(self, text="Du hast alle Vokabeln geschafft!")

        if wrong_vocabs:
            self.show_wrong_vocabs(wrong_vocabs)

        SubmitButton(
            self,
            text="Start Again",
            command=lambda: controller.handle_button(),
        )

    def show_wrong_vocabs(self, wrong_vocabs: str):
        Label(
            self,
            text=(
                "Bei folgenden Vokabeln hast du Fehler gemacht. "
                "Vielleicht willst du sie nochmal genauer anschauen."
            ),
        )
        Label(self, text=wrong_vocabs)
