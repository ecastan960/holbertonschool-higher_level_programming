#!/usr/bin/python3
def max_integer(my_list=[]):
    max1 = 0
    if len(my_list) == 0:
        return None
    for x in my_list:
        if x > max1:
            max1 = x
    return max1