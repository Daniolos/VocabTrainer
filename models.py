import json
import random
import re


class Vocab:
    def __init__(self, data: dict[str, str]) -> None:
        self.german = data.get("German")
        self.english = data.get("English")

    def __hash__(self) -> int:
        return hash(self.german)


class VocabModel:
    def __init__(self, file_name: str):
        self.vocab_list = VocabLoader.load_vocab_list(file_name)

        self.reset()

    @property
    def current_vocab(self):
        return (
            self.current_vocab_list[self.current_vocab_index]
            if self.current_vocab_list
            else None
        )

    @property
    def next_vocab(self):
        if self.is_last_vocab:
            return self.next_list[0] if self.next_list else None

        index = self.current_vocab_index + 1
        return self.current_vocab_list[index]

    @property
    def is_last_vocab(self):
        return self.current_vocab_index >= len(self.current_vocab_list) - 1

    @property
    def next_list(self):
        return (
            self.wrong_vocab_list
            if self.current_vocab_list is self.vocab_list
            else None
        )

    def set_next_vocab(self):
        if not self.is_last_vocab:
            self.current_vocab_index += 1
        else:
            self.current_vocab_index = 0
            self.set_next_list()

    def set_next_list(self):
        self.current_vocab_list = self.next_list

    def reset(self):
        self.wrong_vocab_list = []
        self.current_vocab_index = 0
        self.current_vocab_list = self.vocab_list

    def mark_vocab_wrong(self):
        if self.current_vocab in self.wrong_vocab_list:
            return
        self.wrong_vocab_list.append(self.current_vocab)

    def verify_input(self, input: str) -> bool:
        print(self.comparable(input))
        print(self.comparable(self.current_vocab.english))
        return (
            True
            if self.comparable(input) == self.comparable(self.current_vocab.english)
            else False
        )

    def comparable(self, text: str) -> list[str]:
        text = re.sub(r"\([^\)]*\)", "", text)
        return (
            text.replace("to ", "")
            .replace("the ", "")
            .replace("a ", "")
            .replace("sb.", "somebody")
            .replace("someone", "somebody")
            .strip()
        )


class VocabLoader:
    @classmethod
    def load_vocab_list(cls, file_name: str) -> list[Vocab]:
        with open(file_name, "r", encoding="utf-8") as file:
            vocab_data_list = json.load(file)

        if not cls.validate_format(vocab_data_list):
            raise Exception(
                "The provided JSON data has not a valid format. "
                "Please read the README.md for more information."
            )

        vocab_list = [Vocab(vocab_data) for vocab_data in vocab_data_list]
        random.shuffle(vocab_list)

        return vocab_list

    @staticmethod
    def validate_format(data) -> bool:
        if not isinstance(data, list):
            return False
        for item in data:
            if not isinstance(item, dict):
                return False
            if sorted(item.keys()) != ["English", "German"]:
                return False
            if not all(isinstance(value, str) for value in item.values()):
                return False
        return True
