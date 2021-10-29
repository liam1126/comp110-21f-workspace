"""Practice with dictionaries."""

__author__ = "730323188"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a list."""
    new_dict: dict[str, str] = dict()
    new_keys: str
    new_values: str
    for boop in input:
        new_keys = input[boop]
        new_values = boop
        if new_keys in new_dict:
            raise KeyError("You would have had duplicates keys in the new list. A shame, really.")
        new_dict[new_keys] = new_values
    return new_dict


def favorite_color(input: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    new_dict: dict[str, int] = dict()
    color_name: str
    final_color: str = ""
    maximum: int = 0
    for boop in input:
        color_name = input[boop]
        new_dict[color_name] = 0
    for beep in input:
        color_name = input[beep]
        new_dict[color_name] += 1
        if new_dict[color_name] > maximum:
            maximum = new_dict[color_name]
            final_color = color_name
    return final_color


def count(input: list[str]) -> dict[str, int]:
    """Counts the number of strings in a list."""
    new_dict: dict[str, int] = dict()
    for beep in input:
        if beep in new_dict:
            new_dict[beep] += 1
        else:
            new_dict[beep] = 1
    return new_dict