#!/usr/bin/python3
"""[summary]
"""
import json

def save_to_json_file(my_obj, filename):
    """[summary]

    Args:
        my_obj ([type]): [description]
        filename ([type]): [description]
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json_object = json.dumps(my_obj) 
        f.write(json_object)
