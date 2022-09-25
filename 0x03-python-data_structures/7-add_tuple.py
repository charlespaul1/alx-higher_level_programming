#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)#add the index 0 of a and b together, index 1 of a and b together
    return (tuple_a [0] + tuple_b[0], tuple_a[1] + tuple_b[1])
