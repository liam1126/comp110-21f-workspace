"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count

import pytest

__author__ = "730323188"


def test_invert_empty() -> None:
    """No input."""
    assert invert({}) == {}


def test_invert_single_pair() -> None:
    """One pair of keys and values."""
    assert invert({"lettuce": "tomato"}) == {"tomato": "lettuce"}


def test_invert_many_pairs() -> None:
    """Multiple pairs of keys and values."""
    assert invert({"yes": "no", "up": "down", "left": "right"}) == {"no": "yes", "down": "up", "right": "left"}


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_favorite_color_empty() -> None:
    """No input."""
    assert favorite_color({}) == ""


def test_favorite_color_single_pair() -> None:
    """One pair of person and color."""
    assert favorite_color({"Liam": "blue"}) == "blue"


def test_favorite_color_multiple_pairs() -> None:
    """Multiple pairs of people and colors."""
    assert favorite_color({"Liam": "blue", "Ava": "red", "Megan": "blue"}) == "blue"


def test_favorite_color_tie() -> None:
    """A tie between favorite colors."""
    assert favorite_color({"Liam": "blue", "Ava": "red", "Megan": "blue", "Ellen": "red"}) == "blue"


def test_count_empty() -> None:
    """No input."""
    assert count([]) == {}


def test_count_single_item() -> None:
    """One str in the input list."""
    assert count(["nice"]) == {"nice": 1}


def test_count_multiple_items() -> None:
    """Multiple inputs."""
    assert count(["nice", "sick", "alright", "nice", "ohboy", "sick"]) == {"nice": 2, "sick": 2, "alright": 1, "ohboy": 1}