"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730323188"


def test_only_evens_empty() -> None:
    """No input."""
    assert only_evens([]) == []


def test_only_evens_single_even() -> None:
    """A single even number."""
    assert only_evens([200]) == [200]


def test_only_evens_single_odd() -> None:
    """A single odd number."""
    assert only_evens([19]) == []


def test_only_evens_multiple_mixed() -> None:
    """A normal mix of numbers."""
    assert only_evens([2, 3, 4, 5, 6, 7]) == [2, 4, 6]


def test_sub_empty() -> None:
    """Nothing in list."""
    assert sub([], 0, 2) == []


def test_sub_Kris_example() -> None:
    """The example on the website."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_many_inputs() -> None:
    """A normal mix of numbers."""
    assert sub([1, 2, 3, 4, 5, 6], 2, 5) == [3, 4, 5]


def test_sub_negative_start() -> None:
    """The start value is negative."""
    assert sub([3, 5, 7, 9], -1, 2) == [3, 5]


def test_sub_greater_end() -> None:
    """The end is greater than the length of the list."""
    assert sub([1, 2, 3, 4], 0, 6) == [1, 2, 3, 4]


def test_sub_greater_start() -> None:
    """The start is greater than the length of the list."""
    assert sub([1, 2, 3, 4], 5, 2) == []


def test_sub_big_numbers() -> None:
    """Some bigger numbers to show it works."""
    assert sub([400, 600, 800, 2000], 1, 3) == [600, 800]


def test_concat_both_empty() -> None:
    """Both lists empty."""
    assert concat([], []) == []


def test_concat_first_empty() -> None:
    """First list empty."""
    assert concat([], [2, 4, 6]) == [2, 4, 6]


def test_concat_second_empty() -> None:
    """Second list empty."""
    assert concat([1, 3, 5], []) == [1, 3, 5]


def test_concat_both_single() -> None:
    """One number in each list."""
    assert concat([1], [2]) == [1, 2]


def test_concat_both_full() -> None:
    """Multiple numbers in each list."""
    assert concat([1, 3, 5], [2, 4, 6]) == [1, 3, 5, 2, 4, 6]