#!/usr/bin/python3
"""[summary]

Raises:
    TypeError: [description]
    TypeError: [description]
    ValueError: [description]
    ValueError: [description]
    ValueError: [description]
    TypeError: [description]
    ValueError: [description]
    ValueError: [description]
    TypeError: [description]
    ValueError: [description]
    TypeError: [description]
    ValueError: [description]
    TypeError: [description]
    ValueError: [description]
    TypeError: [description]
    ValueError: [description]

Returns:
    [type]: [description]
"""
from models.base import Base


class Rectangle(Base):
    """[summary]

    Args:
        Base ([type]): [description]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.

        Raises:
            TypeError: [description]
            TypeError: [description]
            ValueError: [description]
            ValueError: [description]
            ValueError: [description]
            TypeError: [description]
            ValueError: [description]
            ValueError: [description]
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id is not None:
            self.id = id
        else:
            super().__init__(id=None)

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

    @property
    def x(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__x

    @property
    def y(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__y

    @width.setter
    def width(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("width must be and integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be and integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("x must be and integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("y must be and integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__height * self.__width

    def display(self):
        """[summary]
        """
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """[summary]
        """
        if any(args):
            counter = 0
            for i in args:
                if counter == 0:
                    self.id = i
                    counter += 1
                elif counter == 1:
                    self.__width = i
                    counter += 1
                elif counter == 2:
                    self.__height = i
                    counter += 1
                elif counter == 3:
                    self.__x = i
                    counter += 1
                elif counter == 4:
                    self.__y = i
                    counter += 1
        else:
            for arg in kwargs:
                if arg == 'id':
                    self.id = kwargs['id']
                elif arg == 'width':
                    self.__width = kwargs['width']
                elif arg == 'height':
                    self.__height = kwargs['height']
                elif arg == 'x':
                    self.__x = kwargs['x']
                elif arg == 'y':
                    self.__y = kwargs['y']

    def to_dictionary(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        dicts = {}
        c = 0
        keys = ['id', 'width', 'height', 'x', 'y']
        values = [self.id, self.__width, self.__height, self.__x, self.__y]
        for i in keys:
            dicts[i] = values[c]
            c += 1
        return dicts
