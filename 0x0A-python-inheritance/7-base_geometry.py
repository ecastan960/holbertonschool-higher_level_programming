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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
