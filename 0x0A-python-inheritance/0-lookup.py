#!/usr/bin/python3
"""Documentation for lookup function
"""


def lookup(obj):
    """function that returns the list of available
    attributes and methods of an object:

    Args:
        obj ([obj]): object from which a list of
        attributes will be listed

    Returns:
        [list]: list of attributes of the object.
    """
    return dir(obj)
