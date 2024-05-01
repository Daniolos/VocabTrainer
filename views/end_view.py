import tkinter as tk

from views.start_view import StartView
from app import App
from views.widgets import Label, SubmitButton


class EndView(tk.Frame):
    def __init__(self, master: App):
        super().__init__(master, padx=200, pady=200)
        Label(self, text="Dies ist Seite Zwei")
        SubmitButton(
            self,
            text="Zurück zu Seite Eins",
            command=lambda: master.show_frame(StartView),
        )
