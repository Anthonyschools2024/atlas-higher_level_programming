#!/usr/bin/python3
"""
unittests for max integer
"""
import unittest

class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_not_integer_elements(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

    def test_not_integer_elements(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.8, 4.2]), 4.2)

    def test_repeat_max(self):
        self.assertEqual(max_integer([1, 2, 3, 3, 2, 1]), 3)

    def test_large(self):
        self.assertEqual(max_integer([1000000, 2000000, 3000000]), 3000000)
if __name__ == '__main__':
    unittest.main()
