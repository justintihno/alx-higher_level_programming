#!/usr/bin/python3
"""Add 2 integers."""


def add_integer(a, b=98):
    """Return the addition of a and b.

    Float to be typecasted to integers before addition.

    Raises:
        TypeError: If a or b is a not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
