import tkinter as tk

from controllers.protocols.end_controller_protocol import EndControllerProtocol
from app import App
from models.answer import Answer
from views.widgets import Label, SubmitButton, TableView


class EndView(tk.Frame):
    def __init__(
        self,
        app: App,
        controller: EndControllerProtocol,
        answer_list: list[Answer],
        wrong_answers: str,
    ):
        self.controller = controller

        super().__init__(app, padx=200, pady=200)
        Label(self, text="Du hast alle Vokabeln geschafft!")

        # self.display_table_view(answer_list)

        if wrong_answers:
            self.display_wrong_exercises(wrong_answers)

        SubmitButton(
            self,
            text="Start Again",
            command=lambda: controller.handle_button(),
        )

    def display_wrong_exercises(self, wrong_exercises: str):
        Label(
            self,
            text=(
                "Bei folgenden Vokabeln hast du Fehler gemacht. "
                "Vielleicht willst du sie nochmal genauer anschauen."
            ),
        )
        Label(self, text=wrong_exercises)

    def display_table_view(self, answer_list: list[Answer]):
        column_data = [
            "No.",
            "Instruction",
            "Answer",
            "Solution",
            "Result",
            "Seconds Needed",
        ]
        row_data = [
            (
                number,
                answer.exercise.assignment,
                answer.value,
                answer.exercise.solution,
                answer.is_correct,
                f"{answer.seconds_needed}s",
            )
            for number, answer in enumerate(answer_list, start=1)
        ]

        TableView(self, column_data, row_data)
