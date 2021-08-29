"""Practice with numeric operators"""
__author__: str = "730323188"

left_side: int = int(input("Left-hand side: "))
right_side: int = int(input("Right-hand side: "))
exponent_value: int = (left_side ** right_side)
division_value: int = (left_side / right_side)
integer_division_value: int = (left_side // right_side)
remainder_value: int = (left_side % right_side)

print(str(left_side) + " ** " + str(right_side) + " is " + str(exponent_value))
print(str(left_side) + " / " + str(right_side) + " is " + str(division_value))
print(str(left_side) + " // " + str(right_side) + " is " + str(integer_division_value))
print(str(left_side) + " % " + str(right_side) + " is " + str(remainder_value))