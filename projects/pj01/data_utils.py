"""Utility functions for pj01 analysis."""

from csv import DictReader

__author__ = "730323188"

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Makes a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        new_vs: list[str] = []
        i: int = 0
        while i < n:
            item_col: list[str] = table[column]
            item: str = item_col[i]
            new_vs.append(item)
            i += 1
        result[column] = new_vs
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for cols in names:
        result[cols] = table[cols]
    return result


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based table combined."""
    result: dict[str, list[str]] = {}
    for column in first:
        result[column] = first[column]
    for cols in second:
        if cols in result:
            result[cols] += second[cols]
        else:
            result[cols] = second[cols]
    return result


def count(vs: list[str]) -> dict[str, int]:
    """Counts the frequency of values in an input list."""
    result: dict[str, int] = {}
    for item in vs:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def average(col: list[str]) -> float:
    """Calculates the average as a float."""
    int_list: list[int] = []
    for a in col:
        num: int = int(a)
        int_list.append(num)  
    return sum(int_list) / len(int_list)


def greater_than(col: list[str], threshold: int) -> list[bool]:
    result: list[bool] = []
    int_list: list[int] = []
    for strings in col:
        int_list.append(int(strings))
    for item in int_list:
        result.append(item > threshold)
    return result


def less_than(col: list[str], threshold: int) -> list[bool]:
    result: list[bool] = []
    int_list: list[int] = []
    for strings in col:
        int_list.append(int(strings))
    for item in int_list:
        result.append(item < threshold)
    return result

def masked(col: list[str], mask: list[bool]) -> list[str]:
    result: list[str] = []
    for i in range(len(mask)):
        if mask[i]:
            result.append(col[i])
    return result


def percentages(vs: dict[str, int]) -> dict[str, str]:
    result: dict[str, str] = {}
    for keys in vs:
        per: float = vs[keys] / 573 * 100
        per = round(per, 2)
        result[keys] = str(per) + "%"
    return result