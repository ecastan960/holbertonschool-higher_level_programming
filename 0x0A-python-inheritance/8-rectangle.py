#!/usr/bin/python3
"""Documentation for class BaseGeometry
"""


class BaseGeometry:
    """[summary]
    """
    def area(self):
        """[summary]

        Raises:
            Exception: [description]
        """
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """[summary]

        Args:
            name ([type]): [description]
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
