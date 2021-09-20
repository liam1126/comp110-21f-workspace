"""Finding duplicate letters in a word."""

__author__ = "730323188"

word: str = input("Enter a word: ")
dup: bool = False
i: int = 0

while i < len(word):
    letter: str = word[i]
    j: int = i + 1
    while j < len(word):
        char: str = word[j]
        if letter == char:
            dup = True
        j = j + 1
    i = i + 1


print("Found duplicate: " + str(dup))