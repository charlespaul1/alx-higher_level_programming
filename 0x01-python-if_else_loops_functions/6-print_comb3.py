#!/usr/bin/python3
for item in range(0, 90):
    if item / 10 < item % 10:
        if item != 89:
            print("{:02}".format((item)), end=", ")
        else:
            print("{:02}".format((item)))
