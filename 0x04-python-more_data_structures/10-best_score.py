#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    b = ''
    v = a_dictionary.values()
    for x in v:
        if x:
            c = 1
        else:
            c = 0
    if c == 0:
        return None
    for y in a_dictionary:
        x = a_dictionary.get(y)
        if x > a:
            b = y
    return b
