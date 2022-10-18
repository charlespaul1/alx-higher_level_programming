#!/usr/bin/python3
"""
    adding two integers a and b
    args:
    a (int) :term 1
    b (int, optional): term 2 defaults to 98
    Raises TypeError (a and b must be integer)
    Returns : sum of a and b
"""


def add_integers(a, b):
    """
    adds a and b
    """
    if not isinstance(a, int) and not isinstance(b, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a + b)
