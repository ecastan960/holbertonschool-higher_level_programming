#!/usr/bin/python3
"""[summary]
"""


def append_write(filename="", text=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".

    Returns:
        [type]: [description]
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
