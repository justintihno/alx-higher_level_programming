#!/usr/bin/python3
"""Define function that check class"""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of a class

    Returns:
        True if obj is exactly an instance of the specified class;
        otherwise False.
    """
    return type(obj) == a_class
