#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    b = ''
    if a_dictionary is None or a_dictionary == {}:
        return None
    for y in a_dictionary:
        x = a_dictionary.get(y)
        if x > a:
            b = y
            a = x
    return b
