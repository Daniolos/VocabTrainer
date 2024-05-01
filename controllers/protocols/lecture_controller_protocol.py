from typing import Protocol


class LectureControllerProtocol(Protocol):
    def start_exercise(self): ...
