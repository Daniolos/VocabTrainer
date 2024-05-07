import re


class AnswerVerifier:
    parenthesis_regex = re.compile(r"\([^\)]*\)")

    def verify(self, input: str, solution: str) -> bool:
        return True if self._comparable(input) == self._comparable(solution) else False

    def _comparable(self, text: str) -> list[str]:
        text = self.parenthesis_regex.sub("", text)
        return (
            text.replace("to ", "")
            .replace("the ", "")
            .replace("a ", "")
            .replace("be ", "")
            .replace("sb.", "somebody")
            .replace("someone", "somebody")
            .strip()
        )
