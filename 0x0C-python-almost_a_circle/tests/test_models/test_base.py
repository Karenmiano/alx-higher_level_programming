#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation
"""

import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """Tests for instantiation of the Base class."""

    def test_no_arg(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_None(self):
        obj1 = Base(None)
        obj2 = Base(None)
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_unique_id(self):
        obj1 = Base(15)
        self.assertEqual(obj1.id, 15)

    def test_nb_instances_after_unique_id(self):
        obj1 = Base()
        obj2 = Base(12)
        obj3 = Base()
        self.assertEqual(obj1.id, obj3.id - 1)

    def test_id_public(self):
        obj = Base(12)
        obj.id = 15
        self.assertEqual(15, obj.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == '__main__':
    unittest.main()
