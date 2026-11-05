import unittest

from square import area, perimeter


class SquareAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_integer_side(self):
        self.assertEqual(area(5), 25)

    def test_float_side(self):
        self.assertAlmostEqual(area(2.5), 6.25)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area(-5)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_integer_side(self):
        self.assertEqual(perimeter(5), 20)

    def test_float_side(self):
        self.assertAlmostEqual(perimeter(0.25), 1.0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_string_side(self):
        with self.assertRaises(TypeError):
            perimeter("5")
