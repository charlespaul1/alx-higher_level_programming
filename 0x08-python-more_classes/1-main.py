#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle('w', 4)
print(my_rectangle.__dict__)

my_rectangle.width = '-1'
my_rectangle.height = 0.9
print(my_rectangle.__dict__)

