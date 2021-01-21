#!/usr/bin/python3
"""[summary]
"""
import json


def class_to_json(obj):
    """[summary]

    Args:
        obj ([type]): [description]

    Returns:
        [type]: [description]
    """
    return obj.__dict__
