#!/usr/bin/python3
"""Documentation for Rectangle Class
"""


class Rectangle:
    """[Rectangle class]
    """
    def __init__(self, width=0, height=0):
        """[summary]

        Args:
            width (int, optional): [description]. Defaults to 0.
            height (int, optional): [description]. Defaults to 0.

        Raises:
            TypeError: [description]
            ValueError: [description]
            TypeError: [description]
            ValueError: [description]
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__width

    @property
    def height(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__height

    @width.setter
    def width(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__height * self.__width

    def perimeter(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if self.__height == 0 or self.__width == 0:
            self.__height = 0
            self.__width = 0
        return 2*self.__height + 2*self.__width

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append('#')
            if i != self.__height - 1:
                rectangle.append('\n')
        return ''.join(rectangle)
