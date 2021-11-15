"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730323188"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize the values attribute of Simpy object to argument passed in."""
        self.values = values

    def __str__(self) -> str:
        """Converts Simpy object to str representation."""
        return f"Simpy({self.values})"

    def fill(self, value: float, num: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        i: int = 0
        self.values = []
        while i < num:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the values attribute with a range of values."""
        assert step != 0.0
        self.values = []
        i: float = start
        while i != stop:
            self.values.append(i)
            i += step

    def sum(self) -> float:
        """Computes and returns the sum of all items in the value attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloads the addition operator for Simpy objects."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        else:
            for nums in self.values:
                result.values.append(nums + rhs)
        return result
