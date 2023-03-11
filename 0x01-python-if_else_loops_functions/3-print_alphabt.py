#!/usr/bin/python3
for character in range(97, 123):
    if character not in (113, 101):
        print("{:c}".format(character), end='')
