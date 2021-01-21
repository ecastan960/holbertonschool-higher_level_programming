#!/usr/bin/python3
"""[summary]
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object:

    Args:
        obj (obj): [description]

    Returns:
        [type]: Dictionary description
    """
    return obj.__dict__
