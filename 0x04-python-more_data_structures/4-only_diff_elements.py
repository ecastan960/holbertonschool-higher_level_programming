#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    z = set_1.difference(set_2)
    z1 = set_2.difference(set_1)
    a = z.union(z1)
    return a