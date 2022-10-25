#!/usr/bin/python3

""" function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    with open(filename, mode="w") as fd:
        nbc = fd.write(text)
    return nbc
