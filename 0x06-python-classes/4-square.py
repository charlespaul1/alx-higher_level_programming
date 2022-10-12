#!/usr/bin/python3
"""define a class called Square"""


class Square:
    """class with size as private instance attribute"""
    def __init__(self, size=0):
        """initialize the class"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """return the current area of square"""
        return(self.__size ** 2)

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def self(size, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
