#!/usr/bin/python3
def uppercase(str):
    a = ""
    for item in str:
        if ord(item) > 96 and ord(item) < 123:
            a += chr(ord(item) - 32)
        else:
            a += item
    print("{}".format(a))
