#!/usr/bin/python3
""" My class module
"""


class Student:
    """ My class
    """

    first_name = ''
    last_name = ''
    age = 0

    def __init__(self, first_name, last_name, age):
        """[summary]

        Args:
            first_name ([type]): [description]
            last_name ([type]): [description]
            age ([type]): [description]
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """[summary]

        Args:
            attrs ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if attrs is None:
            return self.__dict__
        attributes = {}
        if type(attrs) is list:
            for a in attrs:
                if a in self.__dict__.keys():
                    attributes[a] = self.__dict__[a]
            return attributes
