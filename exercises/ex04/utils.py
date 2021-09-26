"""List utility functions."""

__author__ = "730323188"

def all(input: list[int], specific_integer: int) -> bool:
    """Returns True iff all numbers match the indicated number."""
    i: int = 0
    while i < len(input):
        item: int = input[i]
        if item != specific_integer:
            return False
        i += 1
    return True


def is_equal(first: list[int], second: list[int]) -> bool:
    """Returns True iff both lists are equal to one another."""
    i: int = 0
    if len(first) != len(second):
        return False
    while i < len(first):
        first_item: int = first[i]
        second_item: int = second[i]
        if first_item != second_item:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Returns the largest int in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    maximum: int = 0
    while i < len(input):
        char: int = input[i]
        if char > maximum:
            maximum = char
        i += 1
    return maximum