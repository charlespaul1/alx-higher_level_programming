#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads the content of a file
    """
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
