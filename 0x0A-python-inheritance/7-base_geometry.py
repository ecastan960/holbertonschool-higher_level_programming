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
        
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        self.value = value
