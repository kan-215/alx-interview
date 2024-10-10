#!/usr/bin/python3
"""pythone module to  lock boxes"""


def canUnlockAll(boxes):
    """the function determines if all boxes can be unlocked."""
    stack = [0]
    visited = [False for i in range(len(boxes))]
    visited[0] = True
    while stack:
        current_box = stack.pop()
        # Iterate through keys in the current box
        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)
    return False not in visited
