"""Practice with relational operators."""
__author__: str = "730323188"

left_side: int = int(input("Left-hand side: "))
right_side: int = int(input("Right-hand side: "))
less_than_value: bool = bool(left_side < right_side)
at_least_value: bool = bool(left_side >= right_side)
equal_to_value: bool = bool(left_side == right_side)
not_equal_to_value: bool = bool(left_side != right_side)

print(str(left_side) + " < " + str(right_side) + " is " + str(less_than_value))
print(str(left_side) + " >= " + str(right_side) + " is " + str(at_least_value))
print(str(left_side) + " == " + str(right_side) + " is " + str(equal_to_value))
print(str(left_side) + " != " + str(right_side) + " is " + str(not_equal_to_value))