import unittest

from rectangle import area, perimeter


class RectangleAreaTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(10, 0), 0)

    def test_square_mul(self):
        self.assertEqual(area(10, 10), 100)

    def test_different_sides(self):
        self.assertEqual(area(3, 4), 12)

    def test_commutative(self):
        self.assertEqual(area(3, 4), area(4, 3))

    def test_float_sides(self):
        self.assertAlmostEqual(area(1.5, 2), 3.0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area(-3, 4)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_zero_sides(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_different_sides(self):
        self.assertEqual(perimeter(3, 4), 14)

    def test_float_sides(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5), 8.0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4)
