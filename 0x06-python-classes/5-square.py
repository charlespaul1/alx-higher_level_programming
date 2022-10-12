#!/usr/bin/python3
"""define a class square"""


class Square:
    """class square with private attribute instance"""
    def __init__(self, size=0):
        """initialize a new square with size arguments"""
        self.size = size

    def area(self):
        """return the current square area"""
        return(self.__size * self.__size)
    
    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """print the square using hashes #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.size == 0:
            print("")
