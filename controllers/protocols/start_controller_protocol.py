from typing import Protocol


class StartControllerProtocol(Protocol):
    def start_exercise(self): ...
