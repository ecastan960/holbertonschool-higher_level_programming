#!/usr/bin/python3
"""[summary]
"""

import unittest
import models.base
from models.base import Base
# from models.rectangle import Rectangle
# from models.square import Square


class testBase(unittest.TestCase):

    def test_doc_class(self):

        self.assertTrue(len(Base.__doc__) > 0)

    def test_doc_file(self):

        self.assertTrue(len(base.__doc__) > 0)

    def test_doc_init(self):

        self.assertTrue(len(Base.__init__.__doc__) > 0)

    def test_doc_to_json_string(self):

        self.assertTrue(len(Base.to_json_string.__doc__) > 0)

    def test_doc_save_to_file(self):

        self.assertTrue(len(Base.save_to_file.__doc__) > 0)

    def test_doc_from_json_string(self):

        self.assertTrue(len(Base.from_json_string.__doc__) > 0)

    def test_doc_create(self):

        self.assertTrue(len(Base.create.__doc__) > 0)

    def test_doc_load_from_file(self):

        self.assertTrue(len(Base.load_from_file.__doc__) > 0)

    def test_main(self):
        """test main"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
