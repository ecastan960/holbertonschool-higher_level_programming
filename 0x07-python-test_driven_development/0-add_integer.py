#!/usr/bin/python3
"""Documentation for a function that add to integers
"""
def add_integer(a, b=98):
    """[summary]

    Args:
        a ([type]): [description]
        b (int, optional): [description]. Defaults to 98.

    Raises:
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
