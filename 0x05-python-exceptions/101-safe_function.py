#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    """Executes a function

    If error message is caught, a message is
    printed to standard error.

    Returns:
        Result of function else none.
    """

    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return res
