#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = list(sorted((a_dictionary.keys())))
    for i in a:
        print("{}: {}".format(i, a_dictionary[i]))
