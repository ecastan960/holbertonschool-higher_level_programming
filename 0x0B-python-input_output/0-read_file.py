#!/usr/bin/python3
"""[summary]
"""


def read_file(filename=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
    print()
