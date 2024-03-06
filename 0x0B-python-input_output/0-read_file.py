#!/usr/bin/python3
"""Defines a text file reading function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its contents to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
