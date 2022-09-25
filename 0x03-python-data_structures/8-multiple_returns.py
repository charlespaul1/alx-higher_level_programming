#!/usr/bin/python3
def multiple_returns(sentence):
    length_of_str = len(sentence)
    first_char = sentence[0] if length_of_str > 0 else "None"
    tu_ple = length_of_str, first_char
    return(tu_ple)
