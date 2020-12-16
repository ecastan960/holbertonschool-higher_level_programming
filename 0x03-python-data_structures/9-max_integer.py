#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max1 = my_list[0]
    for x in my_list:
        if x > max1:
            max1 = x
    return max1
