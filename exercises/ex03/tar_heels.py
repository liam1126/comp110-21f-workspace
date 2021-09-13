"""An exercise in remainders and boolean logic."""

__author__ = "730323188"

user_int: int = int(input("Enter an int: "))
remainder_tar: int = user_int % 2
remainder_heels: int = user_int % 7

if user_int != 0:
    if remainder_tar == 0 and remainder_heels == 0:
        print("TAR HEELS")
    else:
        if remainder_tar == 0:
            print("TAR")
        else:
            if remainder_heels == 0:
                print("HEELS")
            else:
                print("CAROLINA")
else:
    print("CAROLINA")    