#!/usr/bin/python3
"""[summary]
"""


def inherits_from(obj, a_class):
    """[summary]

    Args:
        obj ([type]): [description]
        a_class ([type]): [description]

    Returns:
        [type]: [description]
    """
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    else:
        return False
