"""List utility functions part 2."""

__author__ = "730323188"


def only_evens(input: list[int]) -> list[int]:
    """Returns a list with only even integers."""
    i: int = 0
    cooler_list: list[int] = list()
    while i < len(input):
        if input[i] % 2 == 0:
            cooler_list.append(input[i])
        i += 1
    return cooler_list 


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Returns a subset of a given list."""
    sub_list: list[int] = list()
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if start > len(a_list) or end <= 0:
        return sub_list
    if len(a_list) != 0:   
        while start < end:
            sub_list.append(a_list[start])
            start += 1
    return sub_list
        

def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Concats first list with second list."""
    combination_list: list[int] = first_list + second_list
    return combination_list