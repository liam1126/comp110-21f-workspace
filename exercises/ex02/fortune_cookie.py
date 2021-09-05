"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730323188"

from random import randint

fortune: int = randint(0, 3)

print("Your fortune cookie says...")

if fortune == 3:
    print("Soon, you will hear the best joke you've ever heard.")
else:
    if fortune == 2:
        print("You will finally find your lucky shirt.")
    else:
        if fortune == 1:
            print("You will be offered a delicious snack in the near future!")     
        else:
            if fortune == 0:
                print("A close friend will share exciting news with you soon.")

print("Now, go spread positive vibes!")