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
    if not list_of_integers:
        return None
    else:
        list_sorted = sorted(list_of_integers)
        max_number = list_sorted[len(list_sorted) - 1]
        return max_number
