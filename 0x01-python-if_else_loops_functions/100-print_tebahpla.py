#!/usr/bin/python3

for i in range(25, -1, -1):
    print("{0}{1}".format(chr(97 + i), chr(65 + i)), end="")
