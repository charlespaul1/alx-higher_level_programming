#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    add = 0
    for arguments in argv[1:]:#argv[1:] lists all arguments
        add += int(arguments)#add  = add + arguments
        print("{}".format(add))
