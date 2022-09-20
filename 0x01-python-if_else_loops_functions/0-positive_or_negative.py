#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#determine if number is greater than 0
if number > 0:
    print("{} is positive".format(number))
#determine if number is 0
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
