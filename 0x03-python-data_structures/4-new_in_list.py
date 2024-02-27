#!/usr/bin/python3
"""function replaces element in list without modifying original"""


def new_in_list(my_list, idx, element):
    length = len(my_list)

    copy_list = my_list[:]

    if 0 <= idx < length:
        copy_list[idx] = element

    return (copy_list)
