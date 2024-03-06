#!/usr/bin/python3
"""Function that lists attribute and methods of an object."""


def lookup(obj):
    """Return a list of available attributes and methods."""
    return (dir(obj))
