from typing import Protocol


class EndControllerProtocol(Protocol):
    def handle_button(self): ...
