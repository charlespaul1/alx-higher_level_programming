#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#finding the lastdigit using modulus
if number > 0:
    lastdigit = number % 10
else:
    lastdigit = number % -10
    print("Last digit of {} is {}".format(number, lastdigit))
#determining if lastdigit is >5 or it is 0 or less than 6 and not 0
if lastdigit > 5:
    print("and is greater than 5")
elif lastdigit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")


