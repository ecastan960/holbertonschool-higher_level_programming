#!/usr/bin/python3
"""File that contains a function to find a peak
"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers

    Args:
        list_of_integers (list): List of unsorted integers

    Returns:
        [type]: Integer of at least one peak
    """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
