#!/usr/bin/python3
"""[summary]
"""

import unittest
from models import square
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testBase(unittest.TestCase):

    def test_doc_class(self):

        self.assertTrue(len(Square.__doc__) > 0)

    def test_doc_file(self):

        self.assertTrue(len(square.__doc__) > 0)

    def test_doc_init(self):

        self.assertTrue(len(Square.__init__.__doc__) > 0)

    def test_doc__str__(self):

        self.assertTrue(len(Square.__str__.__doc__) > 0)

    def test_doc_size(self):

        self.assertTrue(len(Square.size.__doc__) > 0)

    def test_doc_update(self):

        self.assertTrue(len(Square.update.__doc__) > 0)

    def test_doc_to_dictionary(self):

        self.assertTrue(len(Square.to_dictionary.__doc__) > 0)
