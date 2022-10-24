#!/usr/bin/python3
"""checks instance of a class"""


def inherits_from(obj, a_class):
    """"Uses isinstance to check if the obj belongs to a_class or subclasses"""
    return isinstance(obj, a_class) and type(obj) != a_class
