#!/usr/bin/python3
"""simple my list class"""

class MyList(list):
    """simple class MyList, it inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""

        return(sorted(self))
