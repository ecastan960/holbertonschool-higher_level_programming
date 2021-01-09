#!/usr/bin/python3
"""Documentation for a function that add to integers
"""


def add_integer(a, b=98):
    """This function adds two integers

    Args:
        a (int): integer to add
        b (int, optional): integer to add. Defaults to 98.

    Raises:
        TypeError: raises when a its not an integer or float
        TypeError: raises when a its not an integer or float

    Returns:
        [int]: returns the sum of two integers
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
