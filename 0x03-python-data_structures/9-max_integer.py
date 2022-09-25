#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    bigest_int = my_list[0]
    for i in my_list:
        if i > bigest_int:
            bigest_int = i
    return (bigest_int)
