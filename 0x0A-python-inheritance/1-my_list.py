#!/usr/bin/python3
""" a simple MyList class"""


class MyList(list):
    """a simple class that inherits from list"""

    def print_sorted(self):
        """prints a sorted list"""

        print(sorted(self))
