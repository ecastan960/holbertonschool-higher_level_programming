#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for x in range(-1, -len(my_list)-1, -1):
        print("{0:d}".format(my_list[x]))
