#!/usr/bin/python3
"""[summary]

Returns:
    [type]: [description]
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """[summary]

    Args:
        Rectangle ([type]): [description]
    """
    def __init__(self, size, x=0, y=0, id=None):
        """[summary]

        Args:
            size ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.width

    @size.setter
    def size(self, value):
        """[summary]

        Args:
            value ([type]): [description]
        """
        self.width = value
        self.height = value

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
                    self.size = i
                    counter += 1
                elif counter == 2:
                    self.x = i
                    counter += 1
                elif counter == 3:
                    self.y = i
                    counter += 1
        else:
            for arg in kwargs:
                if arg == 'id':
                    self.id = kwargs['id']
                elif arg == 'size':
                    self.size = kwargs['size']
                elif arg == 'x':
                    self.x = kwargs['x']
                elif arg == 'y':
                    self.y = kwargs['y']

    def to_dictionary(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        dicts = {}
        c = 0
        keys = ['id', 'size', 'x', 'y']
        values = [self.id, self.size,  self.x, self.y]
        for i in keys:
            dicts[i] = values[c]
            c += 1
        return dicts
