import unittest

from triangle import area, perimeter


class TriangleAreaTestCase(unittest.TestCase):
    def test_zero_height(self):
        self.assertEqual(area(5, 0), 0)

    def test_integer_values(self):
        self.assertEqual(area(4, 3), 6)

    def test_odd_product(self):
        self.assertAlmostEqual(area(1, 1), 0.5)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            area(4, -3)


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(perimeter(1, 1, 1), 3)

    def test_right_triangle(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_float_sides(self):
        self.assertAlmostEqual(perimeter(0.1, 0.2, 0.25), 0.55)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_triangle_inequality(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10)
