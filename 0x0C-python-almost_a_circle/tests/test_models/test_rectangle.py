#!/usr/bin/python3
"""[summary]
"""

import unittest
from models import rectangle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testBase(unittest.TestCase):

    def test_doc_class(self):

        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_doc_file(self):

        self.assertTrue(len(rectangle.__doc__) > 0)

    def test_doc_init(self):

        self.assertTrue(len(Rectangle.__init__.__doc__) > 0)

    def test_doc_width(self):

        self.assertTrue(len(Rectangle.width.__doc__) > 0)

    def test_doc_height(self):

        self.assertTrue(len(Rectangle.height.__doc__) > 0)

    def test_doc_x(self):

        self.assertTrue(len(Rectangle.x.__doc__) > 0)

    def test_doc_y(self):

        self.assertTrue(len(Rectangle.y.__doc__) > 0)

    def test_doc_area(self):

        self.assertTrue(len(Rectangle.area.__doc__) > 0)

    def test_doc_display(self):

        self.assertTrue(len(Rectangle.display.__doc__) > 0)

    def test_doc__str__(self):

        self.assertTrue(len(Rectangle.__str__.__doc__) > 0)

    def test_doc_update(self):

        self.assertTrue(len(Rectangle.update.__doc__) > 0)

    def test_doc_to_dictionary(self):

        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 0)

    def test_attr(self):
        r1 = Rectangle(10, 2)
        
