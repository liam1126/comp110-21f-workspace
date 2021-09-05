"""Counting letters in a string."""

__author__ = "730323188"

letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i: int = 0
count: int = 0

while i < len(word):
    if word[i] == letter:
        count = count + 1
    i = i + 1

count = str(count)
print("Count: " + count)