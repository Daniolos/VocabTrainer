import json

VOCAB_KEYS = "English" | "German"


def load_and_validate_vocabularies(file_path) -> list[dict[VOCAB_KEYS, str]]:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except json.JSONDecodeError:
        raise ValueError("The file could not be decoded as JSON.")

    if validate_format(data):
        return data

    raise ValueError(
        """JSON format is not valid.
        Each item must be a dictionary with 'German' and 'English' keys."""
    )


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
