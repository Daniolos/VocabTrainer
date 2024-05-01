from typing import Protocol


class ExerciseControllerProtocol(Protocol):
    def handle_button(self): ...
