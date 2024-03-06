#!/usr/bin/python3
"""Defines inherited list """


class MyList(list):
    """implement sorted printing for classs"""

    def print_sorted(self):
        """Print list in sorted ascending order"""
        print(sorted(self))
