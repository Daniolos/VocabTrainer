class Exercise:
    def __init__(self, data: dict[str, str]) -> None:
        self.assignment = data.get("assignment")
        self.solution = data.get("solution")
        self.expected_time = data.get("expected_time")

    def __hash__(self) -> int:
        return hash(self.assignment)
