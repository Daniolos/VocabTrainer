import tkinter as tk
from tkinter import ttk
from typing import Any, Callable


class Label(ttk.Label):
    def __init__(self, master: tk.Misc, text: str) -> None:
        super().__init__(master, text=text, padding=10)
        self.pack(side="top", fill="both", expand=True)


class SubmitButton(ttk.Button):
    def __init__(
        self,
        master: tk.Misc,
        text: str,
        command: Callable[[], Any],
    ) -> None:

        super().__init__(master, text=text, command=command, padding=10)
        self.pack()


class Entry(ttk.Entry):
    def __init__(self, master: tk.Misc, variable: tk.StringVar) -> None:
        super().__init__(master, textvariable=variable)
        self.pack()
