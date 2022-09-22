#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    number_of_elements = len(argv)
    print("{:d} {:s}{:s}".format(number_of_elements - 1, "argument" if number_of_elements <= 2 else "arguments","." if number_of_elements == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
