from typing import Protocol


class EndControllerProtocol(Protocol):
    def start_exercise(self): ...
