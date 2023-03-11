#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print("Number of arguments: 0.")
        print(".")
    else:
        print(f"Number of argument(s): {num_args}.")
        print(":")

    for i, arg in enumerate(args):
        print(f"{i+1}: {arg}")
