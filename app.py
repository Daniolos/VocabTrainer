import tkinter as tk


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry(f"{1_000}x{600}")
        self.state = False

        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self._set_fullscreen(not self.state)

    def end_fullscreen(self, event=None):
        self._set_fullscreen(False)

    def _set_fullscreen(self, state):
        self.state = state
        self.attributes("-fullscreen", state)
