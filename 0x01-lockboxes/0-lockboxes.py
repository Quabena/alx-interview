#!/usr/bin/python3
"""
Module that determines if all lockboxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened starting from box 0.

    Args:
        boxes (list of lists): A list where each index represents a box,
        and each box contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    total_boxes = len(boxes)
    opened = set([0])
    keys_available = set(boxes[0])

    while keys_available:
        current_key = keys_available.pop()
        if current_key < 0 or current_key >= total_boxes:
            continue
        if current_key not in opened:
            opened.add(current_key)
            keys_available.update(boxes[current_key])

    return len(opened) == total_boxes
