"""Drawing forests in a loop."""

__author__ = "730323188"

TREE: str = '\U0001F332'
depth: str = (input("Depth: "))
depth_int: int = int(depth)
tree_concat: str = "" + TREE
i: int = 0

while i < depth_int:
    print(TREE)
    TREE = TREE + tree_concat
    i = i + 1