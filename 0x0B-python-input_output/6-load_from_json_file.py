#!/usr/bin/python3
"""[summary]
"""
import json

def load_from_json_file(filename):
    """[summary]

    Args:
        filename ([type]): [description]

    Returns:
        [type]: [description]
    """
    with open(filename, 'r') as f:
        return json.load(f)
