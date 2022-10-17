#!/usr/bin/python3
"""Rectangle empty class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Init method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """calculating area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width > 0 and self.__height > 0:
            return 2 * (self.__width + self.__height)
        else:
            return 0
    def __str__(self):
        """returniing representation of the rectangle with # hashes"""
        if self.__width > 0 and self.__height > 0:
            return ("\n".join(["".join(["#"
                               for y in range(self.__width)])
                               for x in range(self.__height)]))
        else:
            return ("")
    def __repr__(self):
        """returning formal string representation """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
    def __del__(self):
        """called at instance of deletion"""
        print("Bye rectangle...")