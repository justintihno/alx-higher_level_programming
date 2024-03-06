#!/usr/bin/python3
"""Define inherited classs checking function"""


def inherits_from(obj, a_class):
    """Check if object is an inherited instance of a class.

    Returns:
        True If obj is an inherited instance of a class
        Otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
