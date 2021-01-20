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


class Rectangle(BaseGeometry):
    """[summary]

    Args:
        BaseGeometry ([type]): [description]
    """

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

    def area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__height * self.__width

    def __str__(self):
        """[summary]
        """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """[summary]

    Args:
        Rectangle ([type]): [description]
    """

    def __init__(self, size):
        """[summary]

        Args:
            size ([type]): [description]
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__size * self.__size

    def __str__(self):
        """[summary]
        """
        return("[Square] {}/{}".format(self.__size, self.__size))
