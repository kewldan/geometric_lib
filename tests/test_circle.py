import math
import unittest

from circle import area, perimeter


class CircleAreaTestCase(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_unit_radius(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_integer_radius(self):
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def test_float_radius(self):
        self.assertAlmostEqual(area(0.5), 0.25 * math.pi)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_negative_side(self):
        with self.assertRaises(TypeError):
            area("3")


class CirclePerimeterTestCase(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_unit_radius(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_float_radius(self):
        self.assertAlmostEqual(perimeter(2.5), 5 * math.pi)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_string_args(self):
        with self.assertRaises(TypeError):
            perimeter("2")
