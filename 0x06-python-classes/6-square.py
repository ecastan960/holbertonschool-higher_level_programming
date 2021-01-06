#!/usr/bin/python3
"""Square class documentation"""


class Square:
    """This class holds the size of the square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the class

        Args:
            size (int): the size of the square
            position (tuple): tuple of int for position of square

        Raises:
            TypeError: size input its not an integer
            ValueError: size input its less than zero
            TypeError: position must be a tuple of 2 positive integers
        """
        self.__size = size
        self.__position = position

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
            value (int): the size of the square

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

    @property
    def position(self):
        """private definition of property position

        Return:
            Returns position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set position of the square

        Args:
            value(int) the size of the square

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value,tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Method prints a square of define size"""

        if self.__size == 0:
            print()
        else:
            if self.__position[0] >= 0 and self.__position[1] >= 0:
                for x in range(self.__position[1]):
                    print()
            for l1 in range(self.__size):
                for l3 in range(self.__position[0]):
                    print(" ", end='')
                for l2 in range(self.__size):
                    print("#", end='')
                print()

    def area(self):
        """Method to define a square

        Return:
            Returns the square value of the square
        """
        return self.__size * self.__size
