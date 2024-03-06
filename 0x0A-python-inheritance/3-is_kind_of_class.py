#!/usr/bin/python3
"""Define class and inheritance checking function"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance or inherited instance of a class
    Returns:
        True if obj is an instance of or inherited from the specified class
        otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
