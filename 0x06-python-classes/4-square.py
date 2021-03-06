#!/usr/bin/python3
"""Square class documentation"""


class Square:
    """This class holds the size of the square"""

    def __init__(self, size=0):
        """Initialization of the class

        Args:
            size(int) the size of the square

        Raises:
            TypeError: size input its not an integer
            ValueError: size input its less than zero
        """

        if type(size) == int and size >= 0:
            self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Initialization of the class

        Return:
            Returns size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of size in a property

        Args:
            value(int) the size of the square

        Raises:
            TypeError: size input its not an integer
            ValueError: size input its less than zero
        """
        if type(value) == int and value >= 0:
            self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method to define a square
        Return:
            Returns the square value of the square
        """
        return self.__size * self.__size
