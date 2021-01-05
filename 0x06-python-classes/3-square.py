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

    def area(self):
        """Method to define a square
        """
        return self.__size * self.__size
