from abc import ABC
import tkinter as tk


class ViewController(ABC):
    view: tk.Frame = None

    def display(self):
        self.view.pack()

    def hide(self):
        self.view.pack_forget()
