#!/usr/bin/python3
""" defining a class named Square"""


class Square:
    """class with size as private instance attribute"""
    def __init__(self, size = 0):
        """initializing the class"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """finding the area of the square"""
        return(self.__size ** 2)
