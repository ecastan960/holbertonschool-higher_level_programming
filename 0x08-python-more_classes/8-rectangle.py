#!/usr/bin/python3
"""Documentation for Rectangle Class
"""


class Rectangle:
    """[Rectangle class]
    """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

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
                rectangle.append(str(self.print_symbol))
            if i != self.__height - 1:
                rectangle.append('\n')
        return ''.join(rectangle)

    def __repr__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        string = []
        string.append("Rectangle(")
        string.append(str(self.__width))
        string.append(", ")
        string.append(str(self.__height))
        string.append(")")
        return ''.join(string)

    def __del__(self):
        """[summary]
        """
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise ("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise ("rect_2 must be an instance of Rectangle")
        area_rect1 = rect_1.__width * rect_1.__height
        area_rect2 = rect_2.__width * rect_2.__height
        if area_rect1 > area_rect2:
            return rect_1
        else:
            return rect_2
