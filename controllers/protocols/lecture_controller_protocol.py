from typing import Protocol


class LectureControllerProtocol(Protocol):
    def handle_button(self): ...
