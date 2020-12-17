#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for y in a_dictionary:
        x = new.get(y)
        new.update({y: (x * 2)})
    return new
