#!/usr/bin/python3
"""Documentation for class MyList
"""


class MyList(list):
    """Class that inherits from list

    Args:
        list ([list]): list object
    """
    def print_sorted(self):
        print(sorted(self))
